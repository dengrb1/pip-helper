from tkinter import *
from tkinter import messagebox
import os
import sys


root = Tk()
ml = os.getcwd()
file_error = '文件丢失！请重新安装'
ok = "删除完成"
uninstall = 'pip uninstall'

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
    os.system(f'pip uninstall pygame')
    messagebox.showinfo(uninstall, ok)
def pyglet():
    os.system(f'pip uninstall pyglet')
    messagebox.showinfo(uninstall,ok)
def pyopengl():
    os.system(f'pip uninstall pyopengl')
    messagebox.showinfo(uninstall, ok)
def pyode():
    os.system(f'pip uninstall pyode')
    messagebox.showinfo(uninstall ,ok)
def panda3d():
    os.system(f'pip uninstall panda3d')
    messagebox.showinfo(uninstall ,ok)
def cocos2d():
    os.system(f'pip uninstall cocos2d')
    messagebox.showinfo(uninstall, ok)
def kivy():
    os.system(f'pip uninstall kivy')
    messagebox.showinfo(uninstall, ok)
def arcade():
    os.system(f'pip uninstall arcade')
    messagebox.showinfo(uninstall, ok)
def fh():
    sys.exit()
    pass


# Button
bt_fh = Button(frame, text='返回', command=fh)
bt_pygame = Button(frame, text='pygame删除', command=pygame)
bt_pyglet = Button(frame ,text='pyglet删除', command=pyglet)
bt_pyode = Button(frame, text='pyode删除', command=pyode)
bt_panda3d = Button(frame, text='panda3d删除', command=panda3d)
bt_cocos2d = Button(frame, text='cocos2d删除', command=cocos2d)
bt_kivy = Button(frame ,text='kivy删除', command=kivy)
bt_arcade = Button(frame, text='arcade删除', command=arcade)
bt_pyopengl = Button(frame, text='pyopenGL删除', command=pyopengl)

# pack
Label(root, text='游戏库删除')
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
root.geometry('200x300+100+40')