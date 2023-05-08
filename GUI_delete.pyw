from tkinter import *
from tkinter import messagebox
import os


root = Tk()
ml = os.getcwd()
file_error = '文件丢失！请重新安装'
ok2 = "删除完成"
uninstall = 'pip uninstall'


def pyqt_remove():
    os.system('pip uninstall pyqt5')
    os.systen('pip uninstall PyQtWebEngine')
    messagebox.showinfo('pip uninstall', ok2)
    pass
def wxpython_remove():
    os.system('pip uninstall wxpython')
    messagebox.showinfo('pip uninstall', ok2)
    pass
def pygame_remove():
    os.system('pip uninstall pygame')
    messagebox.showinfo('pip uninstall', ok2)
    pass
def Matplotlib():
    os.system('pip uninstall Matplotlib')
    messagebox.showinfo(uninstall, ok2)
def Seaborn():
    os.system('pip uninstall Seaborn')
    messagebox.showinfo(uninstall, ok2)
def kivy():
    os.system('pip uninstall kivy')
    messagebox.showinfo(uninstall, ok2)
def pysimpleGUI():
    os.system('pip uninstall pysimpleGUI')
    messagebox.showinfo(uninstall, ok2)
def pyside6():
    os.system('pip uninstall pyside6')
    messagebox.showinfo(uninstall ,ok2)
def flexx():
    os.system('pip uninstall flexx')
    messagebox.showinfo(uninstall, ok2)
def fh():
    root.destroy()

# button
bt_pq5 = Button(root, text='pyqt5删除', command=pyqt_remove)
bt_pygame = Button(root, text='pygame删除', command=pygame_remove)
bt_matplotlib = Button(root, text='matplotlib删除', command=Matplotlib)
bt_seaborn = Button(root, text='Seaborn删除', command=Seaborn)
bt_kivy = Button(frame, text='kivy删除', command=kivy)
bt_pyside = Button(frame, text='pyside6删除', command=pyside6)
bt_flexx = Button(frame, text='flexx删除', command=flexx)
bt_pysimpleGUI = Button(frame, text='pysimpleGUI删除', commmand=pysimpleGUI)
bt_wxpython = Button(root, text='wxpython删除', command=wxpython_remove)
bt_fh = Button(root, text='返回', command=fh)

# pack and Label
Label(root, text='GUI删除').pack()
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
root.title('GUI')
root.geometry('200x230+400+500')
root.mainloop()