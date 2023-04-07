from tkinter import *
from tkinter import messagebox
import os


root = Tk()
ok = '安装完成'
install_1 = 'pip install'


def pyinstaller():
    os.system('pip install pyinstaller')
    messagebox.showinfo('pip install', ok)
    pass
def pygame():
    os.system('pip install pygame')
    messagebox.showinfo('pip install', ok)
    pass
def pyqt():
    os.system('pip install pyqt5')
    os.system('pip install PyQtWebEngine')
    messagebox.showinfo('pip install', ok)
    pass
def Requests():
    os.system('pip install Requests')
    messagebox.showinfo('pip install', ok)
    pass
def wxpython():
    os.system('pip install wxpython')
    messagebox.showinfo('pip install', ok)
    pass
def nuitka():
    os.system('pip install nuitka')
    messagebox.showinfo('pip install', ok)
    pass
def pywin32():
    os.system('pip install pywin32')
    messagebox.showinfo(install_1, ok)
    pass
def tqdm():
    os.system('pip install tqdm')
    messagebox.showinfo(install_1, ok)
    pass
def django():
    os.system('pip install django')
    messagebox.showinfo(install_1, ok)
    pass
def numpy():
    os.system('pip install numpy')
    messagebox.showinfo(install_1, ok)
    pass
# 按钮
pip_pyinstaller = Button(root, text='pyinstall安装', command=pyinstaller).pack()
pip_pygame = Button(root, text='pygame安装', command=pygame).pack()
pip_pyqt = Button(root, text='pyqt5安装', command=pyqt).pack()
pip_Requests = Button(root, text='Requests安装', command=Requests).pack()
pip_wxpython = Button(root, text='wxpython安装', command=wxpython).pack()
pip_tqdm = Button(root, text='tqdm安装', command=tqdm).pack()
pip_nuitka = Button(root, text='nuitka安装', command=nuitka).pack()
pip_pywin32 = Button(root, text='pywin32安装', command=pywin32).pack()
pip_django = Button(root, text="django安装", command=django)
pip_numpy = Button(root, text='numpy安装', command=numpy)


# 初始化程序
root.title('安装模式')
root.geometry('200x250+10+0')
root.mainloop()
