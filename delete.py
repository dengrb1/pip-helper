from tkinter import *
from tkinter import messagebox
import os


root = Tk()
root_1 = 'pip uninstall'
ok = '安装完成'
ok2 = '删除完成'
uninstall = 'pip uninstall'


def pyinstaller_remove():
    os.system('pip uninstall pyinstaller')
    messagebox.showinfo('pip uninstall', ok2)
    pass
def pygame_remove():
    os.system('pip uninstall pygame')
    messagebox.showinfo('pip uninstall', ok2)
    pass
def wxpython_remove():
    os.system('pip uninstall wxpython')
    messagebox.showinfo('pip uninstall', ok2)
    pass
def Requests_remove():
    os.system('pip uninstall Requests')
    messagebox.showinfo('pip uninstall', ok2)
    pass
def pyqt_remove():
    os.system('pip uninstall pyqt5')
    os.systen('pip uninstall PyQtWebEngine')
    messagebox.showinfo('pip uninstall', ok2)
    pass
def tqdm_remove():
    os.system('pip uninstall tqdm')
    messagebox.showinfo('pip uninstall', ok2)
    pass
def nuitka_remove():
    os.system('pip uninstall nuitka')
    messagebox.showinfo(uninstall, ok2)
    pass
def pywin32_remove():
    os.system('pip uninstall pywin32')
    messagebox.showinfo(uninstall, ok2)
    pass
def django_remove():
    os.system('pip uninstall django')
    messagebox.showinfo(uninstall, ok2)
    pass
def numpy_remove():
    os.system('pip uninstall numpy')
    messagebox.showinfo(uninstall, ok2)
    pass
# 按钮
remove_pyqt = Button(root, text='pyqt删除', command=pyqt_remove).pack()
remove_pygame = Button(root, text='pygame删除',command=pygame_remove).pack()
remove_wxpython = Button(root, text='wxpython删除', command=wxpython_remove).pack()
remove_Requests = Button(root, text='Requests删除', command=Requests_remove).pack()
remove_pyinstaller = Button(root, text='pyinstaller安装', command=pyinstaller_remove).pack()
remove_tqdm = Button(root, text='tqdm删除', command=tqdm_remove).pack()
remove_nuitka = Button(root, text='nuitka删除', command=nuitka_remove).pack()
remove_pywin32 = Button(root, text='pywin32删除', command=pywin32_remove).pack()
remove_django = Button(root, text='django删除', command=django_remove)
remove_numpy = Button(root ,text="numpy删除", command=numpy_remove)


# 初始化程序
root.title('删除模式')
root.geometry('200x250+0+0')
root.mainloop()