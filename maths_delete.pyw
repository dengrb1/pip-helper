from tkinter import *
from tkinter import messagebox
import os


root = Tk()
ml = os.getcwd()
file_error = '文件丢失，请重新安装'
uninstall = 'pip uninstall'
ok = '删除成功!'
i = '-i https://mirrors.aliyun.com/pypi/simple/' 


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
        messagebox.showerror('pip helper', file_error)
    pass
def Numpy():
    os.system('pip uninstall numpy')
    messagebox.showinfo(uninstall, ok)
def scipy():
    os.system(f'pip uninstall scipy')
    messagebox.showinfo(uninstall, ok)
def sympy():
    os.system(f'pip uninstall sympy')
    messagebox.showinfo(uninstall, ok)
def pandas():
    os.system(f'pip uninstall pandas')
    messagebox.showinfo(uninstall, ok)
def fh():
    root.destroy()


# Button
bt_n = Button(frame, text='Numpy删除', command=Numpy)
bt_scipy = Button(frame, text='scipy删除', command=scipy)
bt_sympy = Button(frame, text='sympy删除', command=sympy)
bt_pandas = Button(frame, text='pandas删除', command=pandas)
bt_fh = Button(frame, text='返回', command=fh)

# pack and Label
Label(root, text='计算类删除')
bt_fh.pack()
bt_n.pack()
bt_scipy.pack()
bt_sympy.pack()
bt_pandas.pack()