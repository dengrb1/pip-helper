import sys
import os
from time import *
from time import sleep
import urllib.request
import webbrowser


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
        print('是否继续启动程序(Y.是，N.不是)?')
        input_xz = str(input('>>>'))
        if input_xz != None:
            if input_xz == 'Y' or 'y':
                open_exe('client')
            elif input_xz == 'N' or 'n':
                sys.exit()
            else:
                print('请输入英文字母!!')
                sleep(1.5)
                pass
            pass
        else:
            print('错误：没有输入文字')
            sleep(1.5)
        return False

# try
def python():
    if sys.version_info.major < 3:
        check_internet()
    else:
        print("error：没有安装pip包管理工具和python3.x")
        sleep(1)
        webbrowser.open('https://python.org/downloads/')
        print("请安装Pip或者python")
        print('是否继续启动程序(Y.是，N.不是)?')
        input_xz = str(input('>>>'))
        if input_xz != None:
            if input_xz == 'Y' or 'y':
                open_exe('client')
            elif input_xz == 'N' or 'n':
                sys.exit()
            else:
                print('请输入英文字母!!')
                sleep(1.5)
                pass
        else:
            print('错误：没有输入文字,默认退出！')
            sleep(1.5)
            sys.exit()
