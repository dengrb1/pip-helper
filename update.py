from tkinter import *
from tkinter import messagebox
import webbrowser
from tkinter.scrolledtext import ScrolledText

update = Tk()
url_update = 'https://kgithub.com/dengrb1/pip-helper/releases'


la_1 = Label(update, text='更新日志').pack()
text = """0.1.0 程序添加平时常用的库下载安装
1.0 正式版本发布；修复特定BUG；修复无法使用
pyqt5库编写浏览器的问题

当前版本:0.1.0"""

text_box = ScrolledText(update)
text_box.insert(END, text)
text_box.configure(state='disabled')


# 定义按钮
def update_now():
    webbrowser.open(url_update)
    messagebox.showinfo('update', '请选择最新版本并下载运行安装程序，然后就可以更新了！')
    pass
def quit_update():
    update.destroy()
    pass
# 按钮设置
text_box.pack(fill=BOTH, expand=1, side=RIGHT)
update_now_bt = Button(update, text='更新到最新版本', command=update_now).pack(side=RIGHT)
quit_window_bt = Button(update, text='返回', command=quit_update).pack(side=RIGHT)


# 初始化程序
update.title('更新日志')
update.geometry('330x250+50+50')
update.mainloop()