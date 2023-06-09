from tkinter import *
from tkinter import messagebox
import sys
from subprocess import call
import os


root = Tk()
ml = os.getcwd()
file_error = '文件丢失，请重新安装'


def jc(exe_name):
    if os.path.exists(os.path.join(ml,f"{exe_name}.exe")):
        os.system(f"start {exe_name}.exe")
    else:
        messagebox.showerror('system',file_error)
    pass
def update_pip():
    os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip')
    messagebox.showinfo('pip helper','更新pip包管理器成功!')
def install():
    jc("install")

def delete():
    jc("delete")

def update():
    jc("update")

def exit_exe():
    root.destroy()
    pass

def eyeryone():
    messagebox.showerror('pip helper', '暂时无法使用，因为程序测试途中出现未知问题......')


# Button and Label
Label(root, text='pip_helper').pack()
Button(root, text='安装模式', command=install).pack()
Button(root, text='删除模式', command=delete).pack()
Button(root, text='更新pip包管理工具', command=update_pip).pack()
Button(root, text='更新日志', command=update).pack()
Button(root, text='退出', command=exit_exe).pack()

Label(root, text='version 1.6 @2023-2024 dengrb1').pack()


# mainloop
root.title('选择')
root.geometry('200x220+400+400')
root.mainloop()