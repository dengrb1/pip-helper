from tkinter import *
from tkinter import messagebox
import time
import os
import webbrowser


root = Tk()
ok = '安装完成'
ok2 = '删除完成'


pip_pyinstaller = Button(root, text="pyinstaller安装")
def pyinstaller(e):
    os.system("pip install pyinstaller")
    messagebox.showinfo("pip", ok)
    pass
pip_pyinstaller.bind('<Button-1>', pyinstaller)


root_update = Button(root, text="pip检测升级")
def update(e):
    messagebox.showerror("pip update", "无法使用！程序出现BUG")
    pass
    '''sc = Tk()
    text1 = Text(sc)
    sc.title("pip_update")
    sc.geometry('300x200+300+200')
    pip_update_1 = text1 + "-m pip install --upgrade pip"
    ok_update = Button(sc, text="确定")
    def ok(e):
        os.system(pip_update_1)
        messagebox.showwarning("pip更新完成")
        pass
    quit_update = Button(sc, text="返回")
    def exit_update(e):
        sc.destroy()
        pass
    text1.pack()
    ok_update.bind('<Button-1>', ok)
    quit_update.bind('Button-1>', exit_update)
    text1.pack()
    ok_update.pack()
    quit_update.pack()
    sc.mainloop()
    pass'''
root_update.bind('<Button-1>', update)


pip_pygame = Button(root, text="pygame库安装")
def pygame(e):
    os.system("pip install pygame")
    messagebox.showwarning("pygame install", ok)
    pass
pip_pygame.bind('<Button-1>', pygame)


pip_pyqt = Button(root, text="pyqt5安装")
def pyqt5(e):
    os.system("pip install pyqt5")
    messagebox.showwarning("pip pyqt5", ok)
    pass
pip_pyqt.bind('<Button-1>', pyqt5)


pip_quit = Button(root, text="exit")
def pip_exit(e):
    root.destroy()
    messagebox.showwarning("pip安装助手", "程序已退出")
    pass
pip_quit.bind('<Button-1>', pip_exit)


pip_update = Button(root, text='更新内容')
def update_root(e):
    update_window_1 = Tk()
    la_1 = Label(update_window_1, text='更新内容')
    la_2 = Label(update_window_1, text='''1.0 程序制作完成
    1.2 程序新增pyqt5、pygame、pyinstaller安装
    1.3 程序加入更新界面，里面只显示更新的内容，不会自动更新！
    1.4 新增Requests库安装和删除
    1.5 新增wxpython库安装和删除
    1.6 加入关于模块
    1.7 新增一个小彩蛋
    stop 本程序将在2023年3月20日正式终止更新''')
    la_3 = Label(update_window_1, text="当前版本：1.5")
    la_1.pack()
    la_2.pack()
    la_3.pack()
    update_window_1.title('更新内容')
    update_window_1.geometry('400x200+500+400')
    update_window_1.mainloop()
    pass
pip_update.bind('<Button-1>', update_root)


# 删除模块代码
remove_open = Button(root ,text='删除库模式')
def remove(e):
    # 初始化程序和定义按钮
    remove_1 = Tk()
    remove_pygame = Button(remove_1, text='删除pygame')
    remove_pyinstaller = Button(remove_1, text='删除pyinstaller')
    remove_pyqt = Button(remove_1, text='删除pyqt5')
    remove_Requests = Button(remove_1, text='删除Requests')
    remove_tqdm = Button(remove_1, text='删除tqdm')
    remove_exit = Button(remove_1, text='返回')
    # def处理运行代码
    def pyinstaller_remove(e):
        os.system('pip uninstall pyinstaller')
        messagebox.showinfo('remove', ok2)
        pass
    def pygame_remove(e):
        os.system('pip uninstall pygame')
        messagebox.showinfo('remove', ok2)
        pass
    def pyqt_remove(e):
        os.system('pip uninstall pyqt5')
        messagebox.showinfo('remove', ok2)
        pass
    def Requests_remove(e):
        os.system('pip uninstall Requests')
        messagebox.showinfo('remove', ok2)
        pass
    def quit_remove(e):
        remove_1.destroy()
        pass
    def tqdm_remove(e):
        os.system('pip uninstall tqdm')
        messagebox.showinfo('pip uninstall', ok2)
        pass
    # 定义按钮的def
    remove_pygame.bind('<Button-1>',pygame_remove)
    remove_pyinstaller.bind('<Button-1>', pyinstaller_remove)
    remove_pyqt.bind('<Button-1>', pyqt_remove)
    remove_Requests.bind('<Button-1>',Requests_remove)
    remove_tqdm.bind('<Button-1>', tqdm_remove)
    remove_exit.bind('<Button-1>', quit_remove)
    # 放置remove模块的按钮
    remove_pygame.pack()
    remove_pyqt.pack()
    remove_pyinstaller.pack()
    remove_Requests.pack()
    remove_tqdm.pack()
    remove_exit.pack()
    # 加载删除库的Gui
    remove_1.title('remove')
    remove_1.geometry('200x200+450+400')
    remove_1.mainloop()
    pass
remove_open.bind('<Button-1>', remove)    


# 安装Requests模块
pip_Requests = Button(root, text='Requests安装')
def Requests(e):
    os.system('pip install Requests')
    messagebox.showinfo('pip Requests', ok)
    pass
pip_Requests.bind('<Button-1>', Requests)


# 安装wxPython模块
pip_wxPython = Button(root, text='wxPython安装')
def wxPython(e):
    os.system('pip installl wxPython')
    messagebox.showinfo('pip wxPython', ok)
    pass
pip_wxPython.bind('<Button-1>', wxPython)


# 关于模块
pip_gk = Button(root, text='关于')
def gk(e):
    gk_window = Tk()
    gk_1 = Label(gk_window, text='pip helper')
    gk_2 = Label(gk_window, text='''此程序是由dengrb1开发和编写
    开源地址和教程:https://github.com/dengrb1/pygk
    作者GitHub：https://github.com/dengrb1
    本程序已停止了更新，请前往github仓库下载最新的pip安装助手重置版

    @ 2023-2024 由pygk团队的dengrb1拥有所有权''')
    def open(_=None):
        webbrowser.open('https://github.com/dengrb1/pygk')
        pass
    def quit_gk(e):
        gk_window.destroy()
        pass
    gk_1.pack()
    gk_2.pack()
    open_url = Button(gk_window, text='打开GitHub仓库', command=open).pack()
    quit_bt = Button(gk_window, text='返回', command=quit_gk).pack()
    gk_window.title('关于')
    gk_window.geometry('310x300')
    gk_window.mainloop()
    pass
pip_gk.bind('<Button-1>', gk)


# 彩蛋程序
pip_cd = Button(root , text='彩蛋解锁')
def cd(e):
    messagebox.showinfo('彩蛋', '彩蛋已删除，你来晚了')
    pass
pip_cd.bind('<Button-1>', cd)


pip_tqdm = Button(root, text='tqdm安装')
def tqdm(e):
    os.system('pip install tqdm')
    messagebox.showinfo('pip install', ok)
    pass
pip_tqdm.bind('<Button-1>', tqdm)


# 按钮放置
root_update.pack()
pip_pygame.pack()
pip_pyqt.pack()
pip_pyinstaller.pack()
pip_Requests.pack()
pip_wxPython.pack()
pip_tqdm.pack()
remove_open.pack()
pip_cd.pack()
pip_update.pack()
pip_quit.pack()


# 加载程序GUI
root.title('pip安装助手')
root.geometry('200x350+300+600')
root.mainloop()
