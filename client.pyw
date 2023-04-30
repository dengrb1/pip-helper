from tkinter import *
from tkinter import messagebox
import platform
import os


root = Tk()
ml = os.getcwd()
System = platform.system()
file_error = '文件丢失，请重新安装'


def jc(exe_name):
    if os.path.exists(os.path.join(ml,f"{exe_name}.exe")):
        os.system(f"start {exe_name}.exe")
    else:
        messagebox.showerror('system',file_error)
    pass
    
def install():
    jc("install")

def delete():
    jc("delete")

def gk():
    jc("gk")

def update():
    jc("update")

def exit_exe():
    root.destroy()
    pass


# Button and Label
Label(root, text='pip_helper').pack()
Button(root, text='安装模式', command=install).pack()
Button(root, text='删除模式', command=delete).pack()
Button(root, text='更新日志', command=update).pack()
Button(root, text='关于', command=gk).pack()
Button(root, text='退出', command=exit_exe).pack()


# mainloop
root.title('启动器')
root.geometry('200x200+400+400')
root.mainloop()