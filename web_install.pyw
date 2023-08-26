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
def Requests():
    os.system('pip install Requests -i https://mirrors.aliyun.com/pypi/simple/')
    messagebox.showinfo('pip install', ok)
    pass
def django():
    os.system('pip install django -i https://mirrors.aliyun.com/pypi/simple/')
    messagebox.showinfo(install, ok)
    pass
def open_exe(exe_name):
    if os.path.exists(os.path.join(ml, f"{exe_name}.exe")):
        os.system(f"start {exe_name}.exe")
    else:
        messagebox.showerror('install', file_error)
        pass
    pass
def fastAPI():
    os.system('pip install fastapi -i https://mirrors.aliyun.com/pypi/simple/')
    messagebox.showinfo(install, ok)
def sanic():
    os.system('pip install sanic -i https://mirrors.aliyun.com/pypi/simple/')
    messagebox.showinfo(install, ok)
def nameko():
    os.system('pip install nameko -i https://mirrors.aliyun.com/pypi/simple/')
    messagebox.showinfo(install, ok)
def pydantic():
    os.system('pip install pydantic -i https://mirrors.aliyun.com/pypi/simple/')
    messagebox.showinfo(install, ok)
def fh():
    root.destroy()


# Button
bt_fh = Button(frame, text='返回', command=fh)
bt_d = Button(frame, text='django安装', command=django)
bt_r = Button(frame, text='Requests安装', command=Requests)
bt_fastapi = Button(frame, text='fastAPI删除', command=fastAPI)
bt_sanic = Button(frame, text='sanic删除', command=sanic)
bt_nameko = Button(frame, text='namekos删除', command=nameko)
bt_pydantic = Button(frame, text='pydantic删除', command=pydantic)


# pack
Label(root, text='web类安装').pack()
bt_fh.pack()
bt_d.pack()
bt_r.pack()
bt_d.pack()
bt_r.pack()
bt_fastapi.pack()
bt_sanic.pack()
bt_nameko.pack()
bt_pydantic.pack()



# mainloop
root.title('web')
root.geometry('200x250+600+400')
root.mainloop()