import tkinter as tk
import os

def register():
    username = username_entry.get()
    password = password_entry.get()
    with open("c:/username.md", "w") as f:
        f.write(f"Username: {username}\nPassword: {password}")
    root.destroy()

root = tk.Tk()
root.title("注册程序")

username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

register_button = tk.Button(root, text="Register", command=register)
register_button.pack()

root.mainloop()
