"""基本上，这个文件都是已经提前写好了下一个版本的内容的
之后几天基本上都会发布最新版本的内容的"""

from tkinter import *
from tkinter.scrolledtext import ScrolledText
import webbrowser
from tkinter import messagebox
import os

root = Tk()
ml = os.getcwd()

def quit_exe():
    root.destroy()
def update_now():
    '''if os.path.exists(os.path.join(ml, "downloads_update_now.exe")):
        os.startfile("downloads_update_now.exe")
    else:
        messagebox.showerror('error','错误：文件不存在')'''
    messagebox.showerror('update', '在线更新模块正在更新,请以后再试吧')

# Label
update_now_bt = Button(root ,text='在线更新', command=update_now).pack(side=RIGHT)
quit_bt = Button(root, text='返回', command=quit_exe).pack(side=RIGHT)
Label(root, text='更新日志').pack()
text = '''当前版本:1.6 (Not beta or demo)

0.1.0 暂无日志
1.0 正式版本。修复BUG；改正更新日志显示问题
1.1 加入机器学习库安装；修复BUG；删除“关于”模块
1.2 加入更多可视化库，都在gui安装和删除类里面；修复一些BUG
1.2.1 加入机器学习库——openai；修复BUG;一键安装所有库正在试验中......
1.3 加入更多GUI库，比如：pyside6, kivy等等；修复一些BUG
1.4 加入pip安装检测；加入更多web类库；修复一些BUG
1.5 加入更多机器学习库；修复一些BUG;修改pip安装检测代
1.5.1 修改pip源，让下载速度变得更加快速！！
1.6 加入更多处理数据库；修复一些BUG；加入WIFI检测；修改更新日志文本放置的位置；加入更新pip包管理工具......'''

text_box = ScrolledText(root)
text_box.pack(fill=BOTH, expand=1)
text_box.insert(END, text)
text_box.configure(state='disabled')


# mainloop
root.title('更新日志')
root.geometry('355x250+400+400')
root.mainloop()
