from tkinter import *
from tkinter import messagebox
import os


root = Tk()
ml = os.getcwd()
file_error = '文件丢失，请重新安装'
ok2 = '删除完成'
uninstall = 'pip uninstall'


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


# Button
bt_r = Button(root, text='Requests删除', command=Requests_remove)
bt_d = Button(root, text='django删除', command=django_remove)
bt_fh = Button(root, text='返回', command=fh)

#pack and Label
Label(root, text='web类删除').pack()
bt_d.pack()
bt_r.pack()
bt_fh.pack()

# mainloop
root.title('web')
root.geometry('150x150+400+800')
root.mainloop()