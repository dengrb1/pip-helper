from tkinter import *
from tkinter import messagebox


update = Tk()
url_update = 'https://github.com/dengrb1/pygk'


la_1 = Label(update, text='更新日志').pack()
la_2 = Label(update, text='''1.0 程序制作完成
1.2 程序新增pyqt5、pygame、pyinstaller安装
1.3 程序加入更新界面，里面只显示更新的内容，不会自动更新！
1.4 新增Requests库安装和删除
1.5 新增wxpython库安装和删除
1.6 加入关于模块
1.7 新增一个小彩蛋
1.8 新增nuitka安装和删除
1.9 新增django库安装和删除
2.0 修改窗口参数''').pack()
la_3 = Label(update, text='当前版本:2.0 (Not beta verison)')

# 定义按钮
def quit_update():
    update.destroy()
    pass
# 按钮设置
quit_window_bt = Button(update, text='返回', command=quit_update)

# 初始化程序
update.title('更新日志')
update.geometry('330x250+50+50')
update.mainloop()