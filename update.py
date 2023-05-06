"""基本上，这个文件都是已经提前写好了下一个版本的内容的
之后几天基本上都会发布最新版本的内容的"""

from tkinter import *
from tkinter.scrolledtext import ScrolledText
import webbrowser
from tkinter import messagebox

root = Tk()

def quit_exe():
    root.destroy()
def update_now():
    webbrowser.open("https://kgithub.com/dengrb1/chatgpt/releases/")
    messagebox.showinfo('update', '请选择最新版本并下载运行安装程序，然后就可以更新了！')

# Label
update_now_bt = Button(root ,text='在线更新', command=update_now).pack(side=RIGHT)
quit_bt = Button(root, text='返回', command=quit_exe).pack(side=RIGHT)
Label(root, text='更新日志').pack()
text = '''0.1.0 暂无日志
1.0 正式版本。修复BUG；改正更新日志显示问题

当前版本:1.0 (Not beta or demo)'''

text_box = ScrolledText(root)
text_box.pack(fill=BOTH, expand=1)
text_box.insert(END, text)
text_box.configure(state='disabled')


# mainloop
root.title('更新日志')
root.geometry('355x250+400+400')
root.mainloop()
