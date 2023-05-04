from tkinter import *
from tkinter import messagebox
import webbrowser

update = Tk()
url_update = 'https://github.com/dengrb1/pygk'


la_1 = Label(update, text='更新日志').pack()
la_2 = Label(update, text='''0.1.0 版本为beta and demo version''').pack()
la_3 = Label(update, text='当前版本:2.0 (Not beta verison)')

# 定义按钮
def update_now():
    webbrowser.open(url_update)
    pass
def quit_update():
    update.destroy()
    pass
# 按钮设置
quit_window_bt = Button(update, text='返回', command=quit_update)

# 初始化程序
update.title('更新日志')
update.geometry('330x250+50+50')
update.mainloop()