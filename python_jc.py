import sys
import os
from time import *
from time import sleep
import urllib.request


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
def check_internet(url='http://www.baidu.com/', timeout=5):
    try:
        urllib.request.urlopen(url, timeout=timeout)
        return True
    except Exception as e:
        print('WIFI连接不正常，请检测wifi连接后再试吧')
        sleep(5)
        return False

# try
try:
    import pip
    check_internet()
    open_exe('client')
except ImportError:
    print("请安装Pip或者python")
    sleep(2)
    sys.exit()