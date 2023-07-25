from tkinter import *
from tkinter import messagebox
import os


root = Tk()
ml = os.getcwd()
file_error = '文件丢失，请重新安装'
install = 'pip install'
ok = '安装成功!'
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
    os.system('pip install numpy -i https://mirrors.aliyun.com/pypi/simple/')
    messagebox.showinfo(install, ok)
def scipy():
    os.system(f'pip install scipy {i}')
    messagebox.showinfo(install, ok)
def sympy():
    os.system(f'pip install sympy {i}')
    messagebox.showinfo(install, ok)
def pandas():
    os.system(f'pip install pandas {i}')
    messagebox.showinfo(install, ok)
def pyomo():
    os.system(f'pip install pyomo {i}')
    messagebox.showinfo(install ,ok)
def gpy():
    os.system(f'pip install gpy {i}')
    messagebox.showinfo(install ,ok)
def pydy():
    os.system(f'pip install pydy {i}')
    messagebox.showinfo(install ,ok)
def fh():
    root.destroy()


# Button
bt_n = Button(frame, text='Numpy安装', command=Numpy)
bt_scipy = Button(frame, text='scipy安装', command=scipy)
bt_sympy = Button(frame, text='sympy安装', command=sympy)
bt_pandas = Button(frame, text='pandas安装', command=pandas)
bt_pyomo = Button(frame , text='pyomo安装', command=pyomo)
bt_gpy = Button(frame ,text='gpy安装', command=gpy)
bt_pydy = Button(frame , text='pydy安装', command=pydy)
bt_fh = Button(frame, text='返回', command=fh)

# pack and Label
Label(root, text='计算类安装')
bt_fh.pack()
bt_n.pack()
bt_scipy.pack()
bt_sympy.pack()
bt_pandas.pack()
bt_pyomo.pack()
bt_gpy.pack()
bt_pydy.pack()


# mainloop
root.title('install')
root.geometry('200x200+10+100')
root.mainloop()