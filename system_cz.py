from tkinter import *
from tkinter import messagebox
import os
import webbrowser


root = Tk()
ok = '安装完成'
ok2 = '删除完成'
uninstall = 'pip uninstall'
install_1 = 'pip install'


# 安装模式
pip_install = Button(root, text='安装模式')
def install(e):
    install = Tk()
    pip_pyinstaller = Button(install, text='pyinstall安装')
    pip_pygame = Button(install, text='pygame安装')
    pip_pyqt = Button(install, text='pyqt5安装')
    pip_Requests = Button(install, text='Requests安装')
    pip_wxpython = Button(install, text='wxpython安装')
    def pyinstaller(e):
        os.system('pip install pyinstaller')
        messagebox.showinfo('pip install', ok)
        pass
    def pygame(e):
        os.system('pip install pygame')
        messagebox.showinfo('pip install', ok)
        pass
    def pyqt(e):
        os.system('pip install pyqt5')
        os.system('pip install PyQtWebEngine')
        messagebox.showinfo('pip install', ok)
        pass
    def Requests(e):
        os.system('pip install Requests')
        messagebox.showinfo('pip install', ok)
        pass
    def wxpython(e):
        os.system('pip install wxpython')
        messagebox.showinfo('pip install', ok)
        pass
    def nuitka(e):
        os.system('pip install nuitka')
        messagebox.showinfo('pip install', ok)
        pass
    def pywin32(e):
        os.system('pip install pywin32')
        messagebox.showinfo(install_1, ok)
        pass
    pip_pyqt.bind('<Button-1>', pyqt)
    pip_pygame.bind('<Button-1>', pygame)
    pip_pyinstaller.bind('<Button-1>', pyinstaller)
    pip_Requests.bind('<Button-1>', Requests)
    pip_wxpython.bind('<Button-1>', wxpython)
    pip_nuitka = Button(install, text='nuitka安装', command=nuitka)
    pip_pywin32 = Button(install, text='pywin32安装', command=pywin32)
    # 载入按钮
    pip_pyqt.pack()
    pip_pygame.pack()
    pip_wxpython.pack()
    pip_Requests.pack()
    pip_pyinstaller.pack()
    pip_nuitka.pack()
    pip_pywin32.pack()
    # 初始化程序
    install.title('安装模式')
    install.geometry('200x200')
    install.mainloop()
    pass
pip_install.bind('<Button-1>', install)    


# 删除模式
pip_remove = Button(root, text='删除模式')
def remove_ms(e):
    remove = Tk()
    remove_pyqt = Button(remove, text='pyqt删除')
    remove_pygame = Button(remove, text='pygame删除')
    remove_wxpython = Button(remove, text='wxpython删除')
    remove_Requests = Button(remove, text='Requests删除')
    remove_pyinstaller = Button(remove, text='pyinstaller安装')
    def pyinstaller_remove(e):
        os.system('pip uninstall pyinstaller')
        messagebox.showinfo('pip uninstall', ok2)
        pass
    def pygame_remove(e):
        os.system('pip uninstall pygame')
        messagebox.showinfo('pip uninstall', ok2)
        pass
    def wxpython_remove(e):
        os.system('pip uninstall wxpython')
        messagebox.showinfo('pip uninstall', ok2)
        pass
    def Requests_remove(e):
        os.system('pip uninstall Requests')
        messagebox.showinfo('pip uninstall', ok2)
        pass
    def pyqt_remove(e):
        os.system('pip uninstall pyqt5')
        os.systen('pip uninstall PyQtWebEngine')
        messagebox.showinfo('pip uninstall', ok2)
        pass
    def tqdm_remove(e):
        os.system('pip uninstall tqdm')
        messagebox.showinfo('pip uninstall', ok2)
        pass
    def nuitka_remove(e):
        os.system('pip uninstall nuitka')
        messagebox.showinfo(uninstall, ok2)
        pass
    def pywin32_remove(e):
        os.system('pip uninstall pywin32')
        messagebox.showinfo(uninstall, ok2)
        pass
    # 定义按钮的def
    remove_pyqt.bind('<Button-1>', pyqt_remove)
    remove_pygame.bind('<Button-1>', pygame_remove)
    remove_pyinstaller.bind('<Button-1>', pyinstaller_remove)
    remove_Requests.bind('<Button-1>', Requests_remove)
    remove_wxpython.bind('<Button-1>', wxpython_remove)
    remove_tqdm = Button(remove, text='tqdm删除', command=tqdm_remove)
    remove_nuitka = Button(remove, text='nuitka删除', command=nuitka_remove)
    remove_pywin32 = Button(remove, text='pywin32删除', command=pywin32_remove)
    # 加载按钮位置
    remove_pyqt.pack()
    remove_pygame.pack()
    remove_wxpython.pack()
    remove_Requests.pack()
    remove_pyinstaller.pack()
    remove_tqdm.pack()
    remove_nuitka.pack()
    remove_pywin32.pack()   
    # 初始化程序
    remove.title('删除模式')
    remove.geometry('200x200')
    remove.mainloop()
    pass
pip_remove.bind('<Button-1>', remove_ms)


# 更新内容
root_update = Button(root, text='更新日志')
def update(e):
    update_window_1 = Tk()
    la_1 = Label(update_window_1, text='更新内容')
    la_2 = Label(update_window_1, text='''1.0 程序制作完成
    1.2 程序新增pyqt5、pygame、pyinstaller安装
    1.3 程序加入更新界面，里面只显示更新的内容，不会自动更新！
    1.4 新增Requests库安装和删除
    1.5 新增wxpython库安装和删除
    1.6 加入关于模块
    1.7 新增一个小彩蛋
    1.8 新增nuitka安装和删除''')
    la_3 = Label(update_window_1, text="当前版本：1.8")
    la_1.pack()
    la_2.pack()
    la_3.pack()
    update_window_1.title('更新内容')
    update_window_1.geometry('400x200')
    update_window_1.mainloop()
    pass
root_update.bind('<Button-1>', update)


# 关于模块
pip_gk = Button(root, text='关于')
def gk(e):
    gk_window = Tk()
    gk_1 = Label(gk_window, text='pip helper重制版')
    gk_2 = Label(gk_window, text='''此程序是由dengrb1开发和编写
    开源地址和教程:https://github.com/dengrb1/pygk
    作者GitHub：https://github.com/dengrb1

    @ 2023-2024 由pygk团队的dengrb1拥有所有权''')
    def quit_gk(_=None):
        gk_window.destroy()
        pass
    def open_url(_=None):
        webbrowser.open('https://github.com/dengrb1/pygk')
        pass
    gk_1.pack()
    gk_2.pack()
    open_web = Button(gk_window, text='打开GitHub仓库地址', command=open_url).pack()
    quit_gk_bt = Button(gk_window, text='返回', command=quit_gk).pack()        
    gk_window.title('关于')
    gk_window.geometry('310x300')
    gk_window.mainloop()
    pass
pip_gk.bind('<Button-1>', gk)


# 彩蛋程序
pip_cd = Button(root , text='彩蛋解锁')
def cd(e):
    messagebox.showinfo('彩蛋', '哦，你来晚了，彩蛋已经被删除了')
    pass
pip_cd.bind('<Button-1>', cd)


# 退出模块
def exit_pip(_=None):
    messagebox.showwarning('pip helper', '程序正在退出')
    root.destroy()
    pass
pip_exit = Button(root, text='退出', command=exit_pip)


# 加载按钮位置（root）
pip_install.pack()
pip_remove.pack()
pip_cd.pack()   
root_update.pack()
pip_gk.pack()
pip_exit.pack()


# 初始化主程序
root.title('pip helper')
root.geometry('200x200+500+400')
root.mainloop()