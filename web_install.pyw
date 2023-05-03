from tkinter import *
from tkinter import messagebox
import os


root = Tk()
ml = os.getcwd()
ok = '安装完成!'
file_error = '文件丢失，请重新安装'
install_1 = 'pip install'


def Requests():
    os.system('pip install Requests')
    messagebox.showinfo('pip install', ok)
    pass
def django():
    os.system('pip install django')
    messagebox.showinfo(install_1, ok)
    pass
def open_exe(exe_name):
    if os.path.exists(os.path.join(ml, f"{exe_name}.exe")):
        os.system(f"start {exe_name}.exe")
    else:
        messagebox.showerror('install', file_error)
        pass
    pass


# button
bt_d = Button(root, text='django安装', command=django)
bt_r = Button(root, text='Requests安装', command=Requests)


# pack and Label
Label(root, text='web类安装').pack()
bt_d.pack()
bt_r.pack()


# mainloop
root.title('web')
root.geometry('150x150')
root.mainloop()