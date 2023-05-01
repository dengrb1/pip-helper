from tkinter import *
from tkinter import messagebox
import os


root = Tk()
ml = os.getcwd()
ok = "install OK!"
install = "Install"

def pyqt5():
    os.system("pip install pyqt5")
    messagebox.showinfo(install, ok)
def wxpython():
    os.system("pip install wxpython")
    messagebox.showinfo(install, ok)
def pygame():
    os.system("pip install pygame")
    messagebox.showinfo(install, ok)


# Button
bt_qt = Button(root, text='pyqt5安装', command=pyqt5)
bt_pygame = Button(root, text='pygame安装', command=pygame)
bt_wx = Button(root, text='wxpython安装', command=wxpython)

# pack and Label
Label(root, text="GUI install").pack()
bt_qt.pack()
bt_pygame.pack()
bt_wx.pack()


# mainloop
root.title("GUI")
root.geometry('200x200+400+400')
root.mainloop()