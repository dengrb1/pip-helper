from tkinter import *
from tkinter import messagebox
import os

# 定义内容和创建主窗口
root = Tk()
ml = os.getcwd()
ok = '安装成功'
install = 'pip install'
file_error = '文件丢失，请重新安装'


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



# def
def open_exe(exe_name):
    if os.path.exists(os.path.join(ml, f"{exe_name}.exe")):
        os.system(f"start {exe_name}.exe")
    else:
        messagebox.showerror('delete', file_error)
    pass
def Requests_remove():
    os.system('pip uninstall Requests')
    messagebox.showinfo('pip uninstall', ok2)
    pass
def django_remove():
    os.system('pip uninstall django')
    messagebox.showinfo(uninstall, ok2)
    pass
def fh():
    root.destroy()
    pass