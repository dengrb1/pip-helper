from tkinter import *
from tkinter import messagebox
import platform
import os


root = Tk()
CURRENT_DIR = os.getcwd()
System = platform.system()
file_error = '文件丢失，请重新安装'


def windows_run():
    if os.path.exists(os.path.join(CURRENT_DIR, "system_cz.exe")):
        os.system("start system_cz.exe")
    else:
        messagebox.showerror('update', '重要文件丢失')

def Not_windows_run():
    if os.path.exists(os.path.join(CURRENT_DIR, "system_command.py")):
        os.system("python system_command.py")
    else:
        messagebox.showerror('update', '重要文件丢失')

def system_jc():
    if System != 'Windows':
        Not_windows_run()
    else:
        windows_run()
        pass
    pass

def update():
    messagebox.showwarning('system', '暂无做完')
    pass

def exit_exe():
    root.destroy()
    pass


# Button and Label
Label(root, text='启动器').pack()
Button(root, text='启动程序', command=system_jc).pack()
Button(root, text='更新日志', command=update).pack()
Button(root, text='退出', command=exit_exe).pack()


# mainloop
root.title('启动器')
root.geometry('200x200+400+400')
root.mainloop()