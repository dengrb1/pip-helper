from tkinter import *
from tkinter import messagebox, ttk


root = Tk()

e1 = ttk.Entry(root)
e2 = ttk.Entry(root)
l1 = ttk.Label(root, text='用户名：')
l2 = ttk.Label(root, text='密码：')


def ok():
    input_username = e1.get()
    input_password = e2.get()
    if input_username and input_password != None:
        with open('password.md','w'):
            pass
        pass
    else:
        pass
    pass


root.mainloop()
