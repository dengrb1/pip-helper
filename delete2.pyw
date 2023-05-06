from tkinter import *
from tkinter import messagebox
import os

# 创建主窗口
root = Tk()

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


# def frame
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
def fh():
    root.destroy()


# Button
remove_GUI = Button(frame, text='GUI类删除', command=GUI_delete).pack()
remove_web = Button(frame, text='web类删除', command=web_delete).pack()
remove_pyinstaller = Button(frame, text='pyinstaller删除', command=pyinstaller_remove).pack()
remove_tqdm = Button(frame, text='tqdm删除', command=tqdm_remove).pack()
remove_nuitka = Button(frame, text='nuitka删除', command=nuitka_remove).pack()
remove_pywin32 = Button(frame, text='pywin32删除', command=pywin32_remove).pack()
remove_numpy = Button(frame ,text="numpy删除", command=numpy_remove).pack()
remove_fh = Button(frame, text='返回', command=fh).pack()


# pack
canvas.pack(side="left", fill="both", expand=True)


# mainloop
root.title("delete")
root.geometry("200x250+400+600")
root.mainloop()