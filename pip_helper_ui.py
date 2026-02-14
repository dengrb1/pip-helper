from __future__ import annotations

import subprocess
import sys
import runpy
from dataclasses import dataclass
from pathlib import Path
import tkinter as tk
from tkinter import messagebox
from typing import Callable, Iterable, List, Sequence

MIRROR_URL = "https://mirrors.aliyun.com/pypi/simple/"
BASE_DIR = Path.cwd()


@dataclass(frozen=True)
class PackageAction:
    label: str
    packages: Sequence[str]


class ScrollWindow:
    def __init__(self, title: str, geometry: str, header: str) -> None:
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(geometry)

        self.canvas = tk.Canvas(self.root, width=280, height=280)
        self.frame = tk.Frame(self.canvas)
        self.frame.bind("<Configure>", lambda _e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        tk.Label(self.frame, text=header).pack()

    def add_button(self, text: str, command: Callable[[], None]) -> None:
        tk.Button(self.frame, text=text, command=command).pack()

    def add_blank_line(self) -> None:
        tk.Label(self.frame, text="").pack()

    def run(self) -> None:
        self.root.mainloop()


def run_pip(action: str, packages: Iterable[str], use_mirror: bool = True) -> bool:
    command: List[str] = [sys.executable, "-m", "pip", action, *packages]
    if use_mirror and action == "install":
        command.extend(["-i", MIRROR_URL])

    completed = subprocess.run(command)
    return completed.returncode == 0


def show_result(success: bool, action: str) -> None:
    title = f"pip {action}"
    if success:
        messagebox.showinfo(title, "操作成功")
    else:
        messagebox.showerror(title, "操作失败，请检查网络或权限")


def make_pip_action(action: str, packages: Sequence[str], use_mirror: bool = True) -> Callable[[], None]:
    def handler() -> None:
        success = run_pip(action=action, packages=packages, use_mirror=use_mirror)
        show_result(success=success, action=action)

    return handler


def _run_script_fallback(exe_name: str) -> bool:
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

    messagebox.showerror("启动失败", "文件丢失，请重新安装")
    return False
