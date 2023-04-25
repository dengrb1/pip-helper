from tkinter import *
from tkinter import ttk

root = Tk()
root.title("注册程序")

username_label = ttk.Label(root, text="用户名:")
username_label.pack()

username_entry = ttk.Entry(root)
username_entry.pack()

password_label = ttk.Label(root, text="密码:")
password_label.pack()

password_entry = ttk.Entry(root, show="*")
password_entry.pack()

def register():
    username = username_entry.get()
    password = password_entry.get()
    with open("c:\\username.md", "w") as f:
        f.write(f"{username},{password}")
        pass
    pass

register_button = ttk.Button(root, text="注册", command=register)
register_button.pack()

root.mainloop()
