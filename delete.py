from tkinter import *
from tkinter import messagebox
import os


root = Tk()
root_1 = 'pip uninstall'
ok = '安装完成'
ok2 = '删除完成'
uninstall = 'pip uninstall'
ml = os.getcwd()
file_error = '文件丢失，请重新安装'


def open_exe(exe_name):
    if os.path.exists(os.path.join(ml, f"{exe_name}.exe")):
        os.system(f"start {exe_name}.exe")
    else:
        messagebox.showerror('install', file_error)
        pass
    pass
def GUI_delete():
    open_exe('GUI_delete')
    pass
def web_delete():
    open_exe('web_delete')
    pass
def pyinstaller_remove():
    os.system('pip uninstall pyinstaller')
    messagebox.showinfo('pip uninstall', ok2)
    pass
def tqdm_remove():
    os.system('pip uninstall tqdm')
    messagebox.showinfo('pip uninstall', ok2)
    pass
def nuitka_remove():
    os.system('pip uninstall nuitka')
    messagebox.showinfo(uninstall, ok2)
    pass
def pywin32_remove():
    os.system('pip uninstall pywin32')
    messagebox.showinfo(uninstall, ok2)
    pass
def numpy_remove():
    os.system('pip uninstall numpy')
    messagebox.showinfo(uninstall, ok2)
    pass
# 按钮
remove_GUI = Button(root, text='GUI类删除', command=GUI_delete).pack()
remove_web = Button(root, text='web类删除', command=web_delete).pack()
remove_pyinstaller = Button(root, text='pyinstaller删除', command=pyinstaller_remove).pack()
remove_tqdm = Button(root, text='tqdm删除', command=tqdm_remove).pack()
remove_nuitka = Button(root, text='nuitka删除', command=nuitka_remove).pack()
remove_pywin32 = Button(root, text='pywin32删除', command=pywin32_remove).pack()
remove_numpy = Button(root ,text="numpy删除", command=numpy_remove)


# 初始化程序
root.title('删除模式')
root.geometry('200x250+0+0')
root.mainloop()