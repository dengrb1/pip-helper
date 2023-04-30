from tkinter import *
from tkinter import messagebox
import webbrowser


gk_window = Tk()
url = 'https://github.com/dengrb1/pygk'


la_1 = Label(gk_window, text='关于').pack()
la_2 = Label(gk_window, text='''此程序是由dengrb1开发和编写
开源地址和教程:https://github.com/dengrb1/pygk
作者GitHub：https://github.com/dengrb1

@ 2023-2024 由pygk团队的dengrb1拥有所有权''').pack()
# 其他按钮
def open_url(_=None):
    webbrowser.open(url)
    pass
def quit_gk():
    gk_window.destroy()
    pass
# 按钮定义
open_bt = Button(gk_window, text='打开作者github仓库', command=open_url).pack()
quit_bt = Button(gk_window, text='返回', command=quit_gk).pack()

# 初始化程序
gk_window.title('关于')
gk_window.geometry('250x200+20+0')
gk_window.mainloop()