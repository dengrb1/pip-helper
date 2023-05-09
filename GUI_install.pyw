from tkinter import *
from tkinter import messagebox
import os


root = Tk()
ml = os.getcwd()
ok = "install OK!"
install = "Install"

# 创建滚动区域的Canvas对象
canvas = Canvas(root, width=280, height=280, scrollregion=(0, 0, 500, 500))

# 创建可滚动区域的Frame对象，并将其添加到Canvas中
frame = Frame(canvas)
frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=frame, anchor="nw")

# 创建Scrollbar对象，并将其绑定到Canvas上
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# 显示Canvas和Scrollbar
canvas.pack(side="left", fill="both", expand=True)



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
def kivy():
    os.system('pip install kivy')
    messagebox.showinfo(install, ok)
def pysimpleGUI():
    os.system('pip install pysimpleGUI')
    messagebox.showinfo(install, ok)
def pyside6():
    os.system('pip install pyside6')
    messagebox.showinfo(install ,ok)
def flexx():
    os.system('pip install flexx')
    messagebox.showinfo(install, ok)


# Button
bt_qt = Button(frame, text='pyqt5安装', command=pyqt5)
bt_pygame = Button(frame, text='pygame安装', command=pygame)
bt_matplotlib = Button(frame, text='matplotlib安装', command=Matplotlib)
bt_seaborn = Button(frame, text='Seaborn安装', command=Seaborn)
bt_kivy = Button(frame, text='kivy安装', command=kivy)
bt_pyside = Button(frame, text='pyside6安装', command=pyside6)
bt_flexx = Button(frame, text='flexx安装', command=flexx)
bt_pysimpleGUI = Button(frame, text='pysimpleGUI安装', command=pysimpleGUI)
bt_wx = Button(frame, text='wxpython安装', command=wxpython)
bt_fh = Button(frame, text='返回', command=fh)

# pack and Label
Label(root, text="GUI").pack()
bt_qt.pack()
bt_pyside.pack()
bt_kivy.pack()
bt_pygame.pack()
bt_matplotlib.pack()
bt_seaborn.pack()
bt_flexx.pack()
bt_pysimpleGUI.pack()
bt_wx.pack()
bt_fh.pack()


# mainloop
root.title("GUI")
root.geometry('200x230+100+110')
root.mainloop()