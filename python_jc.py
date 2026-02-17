import os
import re
import sys
import tempfile
import urllib.request
import webbrowser
from pathlib import Path
from typing import List, Optional, Tuple
from time import strftime
import subprocess
import shutil
import runpy
import tkinter as tk
from tkinter import messagebox

BASE_DIR = Path.cwd()
CLIENT_EXE = "client"
FILE_ERROR = "文件丢失，请重新安装！！"
ERROR_MSG = "错误"
PYTHON_DOWNLOAD_PAGE = "https://www.python.org/downloads/"
WINDOWS_PYTHON_INSTALLER_URL = "https://www.python.org/ftp/python/3.12.9/python-3.12.9-amd64.exe"
MIN_PYTHON_VERSION = (3, 8)


def ask_yes_no(title: str, message: str) -> bool:
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    result = messagebox.askyesno(title, message)
    root.destroy()
    return result


def show_info(title: str, message: str) -> None:
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    messagebox.showinfo(title, message)
    root.destroy()


def show_error(title: str, message: str) -> None:
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    messagebox.showerror(title, message)
    root.destroy()




def _ensure_runtime_paths() -> None:
    candidates = [str(BASE_DIR)]
    meipass = getattr(sys, "_MEIPASS", None)
    if meipass:
        candidates.append(str(Path(meipass)))

    for path in candidates:
        if path and path not in sys.path:
            sys.path.insert(0, path)


def _run_script_fallback(exe_name: str) -> bool:
    _ensure_runtime_paths()
    candidates = [BASE_DIR / f"{exe_name}.pyw", BASE_DIR / f"{exe_name}.py"]
    meipass = getattr(sys, "_MEIPASS", None)
    if meipass:
        base = Path(meipass)
        candidates.extend([base / f"{exe_name}.pyw", base / f"{exe_name}.py"])

    for script_path in candidates:
        if script_path.exists():
            runpy.run_path(str(script_path), run_name="__main__")
            return True

    return False


def open_exe(exe_name: str) -> bool:
    exe_path = BASE_DIR / f"{exe_name}.exe"
    if exe_path.exists():
        subprocess.Popen(str(exe_path), shell=True)
        return True

    if _run_script_fallback(exe_name):
        return True

    show_error("启动失败", FILE_ERROR)
    return False


def check_internet(url: str = "http://www.baidu.com/", timeout: int = 5) -> bool:
    try:
        urllib.request.urlopen(url, timeout=timeout)
        return True
    except Exception:
        timestamp = strftime("%Y-%m-%d %H:%M:%S")
        print(f"{ERROR_MSG} {timestamp}: 网络连接不正常")
        return False


def parse_python_version(version_text: str) -> Optional[Tuple[int, int, int]]:
    match = re.search(r"Python\s+(\d+)\.(\d+)\.(\d+)", version_text)
    if not match:
        return None
    return tuple(int(item) for item in match.groups())


def detect_python() -> Tuple[Optional[Tuple[int, int, int]], Optional[str]]:
    candidates: List[Tuple[Tuple[int, int, int], str]] = []

    current_name = Path(sys.executable).name.lower()
    if "python" in current_name:
        current_version = (sys.version_info.major, sys.version_info.minor, sys.version_info.micro)
        candidates.append((current_version, sys.executable))

    commands = [["python", "--version"], ["python3", "--version"], ["py", "-3", "--version"], ["py", "--version"]]
    for command in commands:
        executable = shutil.which(command[0])
        if not executable:
            continue

        result = subprocess.run(command, capture_output=True, text=True)
        output = (result.stdout or result.stderr).strip()
        version = parse_python_version(output)
        if version:
            candidates.append((version, executable))

    if not candidates:
        return None, None

    best = max(candidates, key=lambda item: item[0])
    return best[0], best[1]


def is_python_supported(version: Optional[Tuple[int, int, int]]) -> bool:
    return bool(version and version >= MIN_PYTHON_VERSION)


def auto_install_python() -> bool:
    if os.name != "nt":
        show_error("无法自动安装", "仅支持 Windows 自动安装 Python。")
        return False

    installer_name = Path(WINDOWS_PYTHON_INSTALLER_URL).name
    installer_path = Path(tempfile.gettempdir()) / installer_name

    show_info("Python 自动安装", "即将下载并安装 Python，请稍候。")
    urllib.request.urlretrieve(WINDOWS_PYTHON_INSTALLER_URL, installer_path)

    install_cmd = [
        str(installer_path),
        "/passive",
        "InstallAllUsers=0",
        "PrependPath=1",
        "Include_pip=1",
        "SimpleInstall=1",
    ]
    completed = subprocess.run(install_cmd)
    return completed.returncode == 0


def ensure_python_ready() -> bool:
    version, path = detect_python()
    if is_python_supported(version):
        print(f"Python 检测通过: {version} ({path})")
        return True

    if version:
        message = (
            f"检测到 Python {version}，但版本低于 {MIN_PYTHON_VERSION}。\n"
            "是否自动下载并安装新版本 Python？"
        )
    else:
        message = "未检测到可用 Python。\n是否自动下载并安装 Python？"

    if not ask_yes_no("Python 环境检测", message):
        webbrowser.open(PYTHON_DOWNLOAD_PAGE)
        return False

    try:
        if auto_install_python():
            new_version, new_path = detect_python()
            if is_python_supported(new_version):
                show_info("安装成功", f"Python 已安装完成: {new_version}\n路径: {new_path}")
                return True
            show_error("安装异常", "安装结束但未检测到可用 Python，请手动检查。")
        else:
            show_error("安装失败", "Python 安装程序执行失败，请手动安装。")
    except Exception as exc:
        show_error("安装失败", f"自动安装失败：{exc}")

    webbrowser.open(PYTHON_DOWNLOAD_PAGE)
    return False


def main() -> None:
    network_ok = check_internet()
    if not network_ok:
        if not ask_yes_no("网络检测", "网络不可用，是否继续启动程序？"):
            sys.exit(1)

    if not ensure_python_ready():
        if not ask_yes_no("继续启动", "Python 环境异常，是否仍继续启动 pip-helper？"):
            sys.exit(1)

    if not open_exe(CLIENT_EXE):
        sys.exit(1)


if __name__ == "__main__":
    main()
