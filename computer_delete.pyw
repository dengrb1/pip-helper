from tkinter import *
from tkinter import messagebox
import os


root = Tk()
ml = os.getcwd()
file_error = '文件丢失，请重新安装'
uninstall = 'pip uninstall'
ok = '删除完成'


# def
def TensorFlow():
    os.system('pip uninstall TensorFlow')
    messagebox.showinfo(uninstall, ok)
def pytorch():
    os.system('pip uninstall pytorch')
    messagebox.showinfo(uninstall, ok)
def fh():
    root.destroy()

# Button
bt_TensorFlow = Button(root, text='TensorFlow删除', command=TensorFlow)
bt_pytorch = Button(root, text='pytorch删除', command=pytorch)
bt_fh = Button(root, text='返回', command=fh)

# pack
Label(root, text='机器学习类库删除').pack()
bt_TensorFlow.pack()
bt_pytorch.pack()
bt_fh.pack()


# mainloop
root.title('delete')
root.geometry('150x150+400+650')
root.mainloop()