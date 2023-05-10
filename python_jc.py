import sys
import os
from time import sleep


ml = os.getcwd()
file_error = '文件丢失，请重新安装！！'


# def
def open_exe(exe_name):
    if os.path.exists(os.path.join(ml, f"{exe_name}.exe")):
        os.system(f"start {exe_name}.exe")
    else:
        print(file_error)
        sleep(1)
    pass


# try
try:
    import pip
    print('pip已经安装！！')
    sleep(0.5)
    open_exe('client')
except ImportError:
    print("请安装Pip或者python")
    sleep(2)
    sys.exit()