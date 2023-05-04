from tkinter import *
from tkinter import messagebox
import webbrowser

update = Tk()
url_update = 'https://kgithub.com/dengrb1/pip-helper/releases'


la_1 = Label(update, text='更新日志').pack()
la_2 = Label(update, text='''0.1.0 版本为beta and demo version''').pack()
la_3 = Label(update, text='当前版本:0.1.0 (beta verison)')

# 定义按钮
def update_now():
    webbrowser.open(url_update)
    messagebox.showinfo('update', '请选择最新版本并下载运行安装程序，然后就可以更新了！')
    pass
def quit_update():
    update.destroy()
    pass
# 按钮设置
quit_window_bt = Button(update, text='返回', command=quit_update)
update_now_bt = Button(update, text='更新到最新版本', command=update_now)

# Button pack
update_now_bt.pack()
quit_window_bt.pack()

# 初始化程序
update.title('更新日志')
update.geometry('330x250+50+50')
update.mainloop()