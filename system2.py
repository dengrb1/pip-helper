# 初始化程序
import os
import webbrowser
import time


# 定义变量
pyinstaller_setup = 'pip install pyinstaller'
pygame_setup = 'pip install pygame'
pyqt_setup = 'pip install pyqt5'
root_text = '1.安装模式，2.删除模式，3更新日志，4.关于，5.退出'
# root_text = '1.pyinstaller安装，2.pygame安装，3.pyqt5安装，4.更新日志，5.删除模式，6.退出,7.Requests安装'
setup_ok = '安装完成'
clean = 'cls'
root_2 = '1.删除pyinstaller，2.删除pygame，3删除pyqt5，4.Requests删除,5.tqdm删除'
remove_pyinstaller = 'pip uninstall pyinstaller'
remove_pygame = 'pip uninstall pygame'
remove_pyqt5 = 'pip uninstall pyqt5'
remove = '删除完成'
remove_Requests = 'pip uninstall Requests'
Requests_setup = 'pip install Requests'
install_text = '1.pyinstaller安装，2.pygame安装，3.pyqt5安装，4.Requests安装,5.返回，6.tqdm安装,7.wxpython安装,8.nuitka安装,9.返回'


# 选择模块测试
while 1:
    print(root_text)
    xz = int(input('请选择'))
    if xz == 1:
        while 1:
            print(install_text)
            xz_install = int('请选择：')
            if xz_install == 1:
                os.system(pyinstaller_setup)
                print(setup_ok)
                time.sleep(1)
                pass
            elif xz_install == 2:
                os.system(pygame_setup)
                print(setup_ok)
                time.sleep(1)
                pass
            elif xz_install == 3:
                os.system(pyqt_setup)
                os.system('pip install PyQtWebEngine')
                print(setup_ok)
                time.sleep(1)
                pass
            elif xz_install == 4:
                os.system(Requests_setup)
                print(setup_ok)
                time.sleep(1)
                pass
            elif xz_install == 5:
                break
            elif xz_install == 6:
                os.system('pip install tqdm')
                print(setup_ok)
                time.sleep(1)
                pass
            elif xz_install == 7:
                os.system('pip install wxpython')
                print(setup_ok)
                time.sleep(1)
                pass
            elif xz_install == 8:
                os.system('pip install nuitka')
                print(setup_ok)
                time.sleep(0.5)
                pass
            elif xz_install == 9:
                break
            pass
        pass
    elif xz == 2:
        while 1:
            remove_text = '1.pyinstaller删除，2.pygame删除，3.pyqt5删除，4.Requests删除，5.wxpython删除，6.tqdm删除,nuitka安装，8.返回'
            print(remove_text)
            xz_remove = int(input('请选择：'))
            if xz_remove == 1:
                os.system(remove_pyinstaller)
                print(remove)
                time.sleep(1)
                pass
            elif xz_remove == 2:
                os.system(remove_pygame)
                print(remove)
                time.sleep(1)
                pass
            elif xz_remove == 3:
                os.system(remove_pyqt5)
                os.system('pip uninstall PyQtWebEngine')
                print(remove)
                time.sleep(1)
                pass
            elif xz_remove == 4:
                os.system(remove_Requests)
                print(remove)
                time.sleep(1)
                pass
            elif xz_remove == 45:
                os.system('pip uninstall wxpython')
                print(remove)
                time.sleep(1)
                pass
            elif xz_remove == 6:
                os.system('pip uninstall tqdm')
                print(remove)
                time.sleep(1)
                pass
            elif xz_remove == 7:
                os.system('pip uninstall nuitka')
                print(remove)
                time.sleep(0.5)
                pass
            elif xz_remove == 8:
                break
            else:
                print('error:不支持这个参数')
                time.sleep(0.86)
                pass
            pass
        pass
    elif xz == 402:
        print('哦，你来晚了，彩蛋已经删除了')
        time.sleep(1)
        pass
    elif xz == 3:
        while True:
            print('更新日志')
            print('''1.0 程序制作完成
            1.2 程序新增pyqt5、pygame、pyinstaller安装
            1.3 程序加入更新界面，里面只显示更新的内容，不会自动更新！
            1.4 新增Requests库安装和删除
            1.5 新增wxpython库安装和删除
            1.6 加入关于模块
            1.7 新增一个小彩蛋
            1.8 新增nuitka安装和删除''')
            print('当前版本:1.8')
            if int(input('继续看?' + '1是，2不是')) == 1:
                continue
            else:
                break
            pass
    elif xz == 4:
        while True:
            print('关于')
            print('''此程序是由dengrb1开发和编写
            开源地址和教程:https://github.com/dengrb1/pygk
            作者GitHub：https://github.com/dengrb1

            @ 2023-2024 由pygk团队的dengrb1拥有所有权''')
            if int(input('是否打开GitHub仓库地址？' + '1是，2不是')) == 1:
                webbrowser.open('https://github.com/dengrb1/pygk')
                pass
            else:
                pass  
            if int(input('继续看?' + '1是，2不是')) == 1:
                continue
            else:
                break
        pass
    elif xz == 5:
        break          
    pass


# 程序退出模块(已被废弃)
print('程序退出')
time.sleep(0.62)
exit()

