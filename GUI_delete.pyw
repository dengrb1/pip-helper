from tkinter import *
from tkinter import messagebox
import os


root = Tk()
ml = os.getcwd()
file_error = '文件丢失！请重新安装'
ok2 = "删除完成"
uninstall = 'pip uninstall'

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



def pyqt():
    os.system('pip uninstall pyqt5')
    os.systen('pip uninstall PyQtWebEngine')
    messagebox.showinfo('pip uninstall', ok2)
    pass
def wxpython():
    os.system('pip uninstall wxpython')
    messagebox.showinfo('pip uninstall', ok2)
    pass
def pygame():
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
bt_qt = Button(root, text='pyqt5删除', command=pyqt)
bt_pygame = Button(root, text='pygame删除', command=pygame)
bt_wx = Button(frame, text='wxpython删除', command=wxpython)
bt_kivy = Button(frame, text='kivy删除', command=kivy)
bt_pyside = Button(frame, text='pyside6删除', command=pyside6)
bt_flexx = Button(frame, text='flexx删除', command=flexx)
bt_matplotlib = Button(frame, text='matplatlib删除', command=Matplotlib)
bt_seaborn = Button(frame, text='seaborn删除', command=Seaborn)
bt_pysimpleGUI = Button(frame, text='pysimpleGUI删除', command=pysimpleGUI)
bt_fh = Button(frame, text='返回', command=fh)

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
root.geometry('200x300+100+100')
root.mainloop()