from tkinter import *
from tkinter import messagebox
import os


root = Tk()
ok = '安装完成'
install_1 = 'pip install'
ml = os.getcwd()
file_error = '文件丢失，请重新安装'



def open_exe():
    if os.path.exists(os.path.join(ml, f"{exe_name}.exe")):
        os.system(f"start {exe_name}.exe")
    else:
        messagebox.showerror('install', file_error)
        pass
    pass
def gui_install():
    open_exe('GUI_install')
def web_install():
    open_exe('web_install')
def pyinstaller():
    os.system('pip install pyinstaller')
    messagebox.showinfo('pip install', ok)
    pass
def nuitka():
    os.system('pip install nuitka')
    messagebox.showinfo('pip install', ok)
    pass
def pywin32():
    os.system('pip install pywin32')
    messagebox.showinfo(install_1, ok)
    pass
def tqdm():
    os.system('pip install tqdm')
    messagebox.showinfo(install_1, ok)
    pass
def numpy():
    os.system('pip install numpy')
    messagebox.showinfo(install_1, ok)
    pass
# 按钮
pip_gui = Button(root, text='GUI类安装', command=gui_install).pack()
pip_web = Button(root, text='web类安装', command=web_install).pack()
pip_pyinstaller = Button(root, text='pyinstall安装', command=pyinstaller).pack()
pip_tqdm = Button(root, text='tqdm安装', command=tqdm).pack()
pip_nuitka = Button(root, text='nuitka安装', command=nuitka).pack()
pip_pywin32 = Button(root, text='pywin32安装', command=pywin32).pack()
pip_numpy = Button(root, text='numpy安装', command=numpy)


# 初始化程序
root.title('安装模式')
root.geometry('200x250+10+0')
root.mainloop()
