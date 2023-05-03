from tkinter import *
from tkinter import messagebox
import os


root = Tk()
ml = os.getcwd()
file_error = '文件丢失！请重新安装'
ok2 = "删除完成"


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

# button
bt_pq5 = Button(root, text='pyqt5删除', command=pyqt_remove)
bt_pygame = Button(root, text='pygame删除', command=pygame_remove)
bt_wxpython = Button(root, text='wxpython删除', command=wxpython_remove)

# pack and Label
Label(root, text='GUI删除').pack()
bt_pq5.pack()
bt_pygame.pack()
bt_wxpython.pack()


# mainloop
root.title('GUI')
root.geometry('200x200+400+500')
root.mainloop()