import sys
import os
import urllib.request
import webbrowser
from time import sleep, strftime
import subprocess


ml = os.getcwd()
file_error = '文件丢失，请重新安装！！'
ERROR_MSG = '错误：'


def open_exe(exe_name):
    if os.path.exists(os.path.join(ml, f"{exe_name}.exe")):
        subprocess.Popen(f"{exe_name}.exe", shell=True)
    else:
        print(file_error)
        sleep(1)


def check_internet(url='http://www.baidu.com/', timeout=5):
    try:
        urllib.request.urlopen(url, timeout=timeout)
        open_exe('client')
        return True
    except Exception as e:
        print(f'{ERROR_MSG}{strftime("%Y-%m-%d %H:%M:%S")}: WIFI连接不正常，请检测wifi连接后再试吧')
        sleep(5)
        print('是否继续启动程序(Y.是，N.不是)?')
        input_xz = str(input('>>>'))
        if input_xz != None:
            if input_xz.lower() == 'y':
                open_exe('client')
            elif input_xz.lower() == 'n':
                sys.exit()
            else:
                print('请输入英文字母!!')
                sleep(1.5)
        else:
            print('错误：没有输入文字')
            sleep(1.5)
        return False








'''def check_python_installation():
    if sys.version_info.major < 3:
        python_path = None
        # 检查是否有 Python 安装目录
        for path in os.environ['PATH'].split(os.pathsep):
            python_exe = os.path.join(path, 'python.exe')
            if os.path.isfile(python_exe):
                python_path = os.path.dirname(python_exe)
                break

        if python_path:
            print(f'{ERROR_MSG}{strftime("%Y-%m-%d %H:%M:%S")}: Python已安装，但版本太低，请安装 Python 3.x 版本')
            webbrowser.open('https://python.org/downloads/')
        else:
            print(f'{ERROR_MSG}{strftime("%Y-%m-%d %H:%M:%S")}: Python未安装，请安装 Python 3.x 版本')
            webbrowser.open('https://python.org/downloads/')
    
            print('是否继续启动程序(Y.是，N.不是)?')
            input_xz = str(input('>>>'))
            if input_xz != None:
                if input_xz.lower() == 'y':
                    open_exe('client')
                elif input_xz.lower() == 'n':
                    sys.exit()
                else:
                    print('请输入英文字母!!')
                    sleep(1.5)
            else:
                print('错误：没有输入文字,默认退出！')
                sleep(1.5)
                sys.exit()
    else:
        python_path = None
        for path in os.environ['PATH'].split(os.pathsep):
            python_exe = os.path.join(path, 'python.exe')
            if os.path.isfile(python_exe):
                python_path = os.path.dirname(python_exe)
                break

        if python_path:
            print('自检正常！')
            open_exe('client')
        else:
            print(f'{ERROR_MSG}{strftime("%Y-%m-%d %H:%M:%S")}: Python未安装，请安装 Python 3.x 版本')
            webbrowser.open('https://python.org/downloads/')
    
            print('是否继续启动程序(Y.是，N.不是)?')
            input_xz = str(input('>>>'))
            if input_xz != None:
                if input_xz.lower() == 'y':
                    open_exe('client')
                elif input_xz.lower() == 'n':
                    sys.exit()
                else:
                    print('请输入英文字母!!')
                    sleep(1.5)
            else:
                print('错误：没有输入文字,默认退出！')
                sleep(1.5)
                sys.exit()'''

if __name__ == "__main__":
    check_internet()
    os.system("taskkill -f -im python_jc.exe")
    sys.exit()
