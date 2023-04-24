from tkinter import *
from tkinter import ttk, messagebox
import hashlib

# 定义用户名和密码
username = 'admin'
password_hash = hashlib.sha256('0000'.encode('utf-8')).hexdigest()

def validate_password():
    input_user = username_entry.get()
    input_pass = hashlib.sha256(password_entry.get().encode('utf-8')).hexdigest()

    if input_user == username and input_pass == password_hash:
        messagebox.showinfo('Login', '密码正确')
        password_entry.delete(0, END)
    else:
        messagebox.showerror('Login', '密码错误')
        password_entry.delete(0, END)

# 创建主窗口
root = Tk()
root.title('Login')

# 创建样式
style = ttk.Style()

style.theme_use('clam')
style.configure('TLabel', font=('Arial', 12))
style.configure('TEntry', font=('Arial', 12))

# 创建用户名和密码输入框
username_entry = ttk.Entry(root, width=30)
username_entry.insert(0, 'Username')
username_entry.configure(foreground='grey')
username_entry.bind('<FocusIn>', lambda event: username_entry.delete(0, END))
username_entry.bind('<FocusOut>', lambda event: username_entry.insert(0, 'Username') if not username_entry.get() else None)

password_entry = ttk.Entry(root, width=30, show='*')
password_entry.insert(0, 'Password')
password_entry.configure(foreground='grey')
password_entry.bind('<FocusIn>', lambda event: password_entry.delete(0, END))
password_entry.bind('<FocusOut>', lambda event: password_entry.insert(0, 'Password') if not password_entry.get() else None)

# 创建"OK"按钮
ok_button = ttk.Button(root, text='OK', command=validate_password)

# 布局
username_entry.pack(pady=10)
password_entry.pack(pady=10)
ok_button.pack(pady=10)

# 运行主循环
root.mainloop()
