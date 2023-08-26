import os
import sys
from tkinter import *
from tkinter import messagebox

root = Tk()
ml = os.getcwd()
ok = "install OK!"
install = "Install"
i = "-i https://mirrors.aliyun.com/pypi/simple/"

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
def pygame():
    os.system(f'pip install pygame {i}')
    messagebox.showinfo(install, ok)
def pyglet():
    os.system(f'pip install pyglet {i}')
    messagebox.showinfo(install,ok)
def pyopengl():
    os.system(f'pip install pyopengl {i}')
    messagebox.showinfo(install, ok)
def pyode():
    os.system(f'pip install pyode {i}')
    messagebox.showinfo(install ,ok)
def panda3d():
    os.system(f'pip install panda3d {i}')
    messagebox.showinfo(install ,ok)
def cocos2d():
    os.system(f'pip install cocos2d {i}')
    messagebox.showinfo(install, ok)
def kivy():
    os.system(f'pip install kivy {i}')
    messagebox.showinfo(install, ok)
def arcade():
    os.system(f'pip install arcade {i}')
    messagebox.showinfo(install, ok)
def fh():
    sys.exit()
    pass


# Button
bt_fh = Button(frame, text='返回', command=fh)
bt_pygame = Button(frame, text='pygame安装', command=pygame)
bt_pyglet = Button(frame ,text='pyglet安装', command=pyglet)
bt_pyode = Button(frame, text='pyode安装', command=pyode)
bt_panda3d = Button(frame, text='panda3d安装', command=panda3d)
bt_cocos2d = Button(frame, text='cocos2d安装', command=cocos2d)
bt_kivy = Button(frame ,text='kivy安装', command=kivy)
bt_arcade = Button(frame, text='arcade安装', command=arcade)
bt_pyopengl = Button(frame, text='pyopenGL安装', command=pyopengl)

# pack
Label(root, text='游戏库安装')
bt_fh.pack()
bt_pygame.pack()
bt_pyopengl.pack()
bt_pyglet.pack()
bt_pyode.pack()
bt_panda3d.pack()
bt_cocos2d.pack()
bt_kivy.pack()
bt_arcade.pack()


# mainloop
root.title('game')
root.geometry('200x300+100+80')
root.mainloop()

