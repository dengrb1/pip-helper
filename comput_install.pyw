from tkinter import *
from tkinter import messagebox
import os


root = Tk()
ml = os.getcwd()
file_error = '文件丢失，请重新安装'
ok = '安装完成'
install = 'pip install'


# def
def tensorFlow():
    os.system('pip install TensorFlow')
    messagebox.showinfo(install, ok)
def pytorch():
    os.system('pip install pytorch')
    messagebox.showinfo(install, ok)
def fh():
    root.destroy()

# Button
bt_tensorFlow = Button(root, text='TensorFlow安装', command=tensorFlow)
bt_pytorch = Button(root, text='pytorch安装', command=pytorch)
bt_fh = Button(root, text='返回', command=fh)

# pack
Label(root, text='机器学习类库安装').pack()
bt_tensorFlow.pack()
bt_pytorch.pack()
bt_fh.pack()


# mainloop
root.title('install')
root.geometry('150x150+400+700')
root.mainloop()