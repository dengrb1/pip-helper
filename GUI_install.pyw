from tkinter import *
from tkinter import messagebox
import os


root = Tk()
ml = os.getcwd()
ok = "install OK!"
install = "Install"

def pyqt5():
    os.system("pip install pyqt5")
    os.systen('pip install PyQtWebEngine')
    messagebox.showinfo(install, ok)
def wxpython():
    os.system("pip install wxpython")
    messagebox.showinfo(install, ok)
def pygame():
    os.system("pip install pygame")
    messagebox.showinfo(install, ok)
def Matplotlib():
    os.system('pip install Matplotlib')
    messagebox.showinfo(install, ok)
def Seaborn():
    os.system('pip install Seaborn')
    messagebox.showinfo(install, ok)
def fh():
    root.destroy()


# Button
bt_qt = Button(root, text='pyqt5安装', command=pyqt5)
bt_pygame = Button(root, text='pygame安装', command=pygame)
bt_matplotlib = Button(root, text='matplotlib安装', command=Matplotlib)
bt_seaborn = Button(root, text='Seaborn安装', command=Seaborn)
bt_wx = Button(root, text='wxpython安装', command=wxpython)
bt_fh = Button(root, text='返回', command=fh)

# pack and Label
Label(root, text="GUI").pack()
bt_qt.pack()
bt_pygame.pack()
bt_matplotlib.pack()
bt_seaborn.pack()
bt_wx.pack()
bt_fh.pack()


# mainloop
root.title("GUI")
root.geometry('200x230+400+400')
root.mainloop()