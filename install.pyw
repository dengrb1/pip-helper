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
    messagebox.showinfo(install, ok)
    pass
def tqdm():
    os.system('pip install tqdm')
    messagebox.showinfo(install, ok)
    pass
def numpy():
    os.system('pip install numpy')
    messagebox.showinfo(install, ok)
    pass
def fh():
    root.destroy()

# Button
pip_gui = Button(frame, text='GUI类安装', command=gui_install).pack()
pip_web = Button(frame, text='web类安装', command=web_install).pack()
pip_pyinstaller = Button(frame, text='pyinstall安装', command=pyinstaller).pack()
pip_tqdm = Button(frame, text='tqdm安装', command=tqdm).pack()
pip_nuitka = Button(frame, text='nuitka安装', command=nuitka).pack()
pip_pywin32 = Button(frame, text='pywin32安装', command=pywin32).pack()
pip_numpy = Button(frame, text='numpy安装', command=numpy).pack()
pip_fh = Button(frame,text='返回', command=fh).pack()


# mainloop
root.title('安装')
root.geometry('200x250+400+600')
root.mainloop()