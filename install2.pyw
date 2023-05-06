from tkinter import *
from tkinter import messagebox
import os

# 创建主窗口
root = tk.Tk()
root.title("Scrollable Button Grid")
root.geometry("300x300")

# 创建滚动区域的Canvas对象
canvas = tk.Canvas(root, width=280, height=280, scrollregion=(0, 0, 500, 500))

# 创建可滚动区域的Frame对象，并将其添加到Canvas中
scroll_frame = tk.Frame(canvas)
scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

# 创建Scrollbar对象，并将其绑定到Canvas上
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# 在Frame中添加多个Button对象
for i in range(50):
    button = tk.Button(scroll_frame, text=f"Button {i+1}")
    button.pack(pady=5)

# 显示Canvas和Scrollbar
canvas.pack(side="left", fill="both", expand=True)
