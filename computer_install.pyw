from tkinter import *
from tkinter import messagebox
import os


root = Tk()
ml = os.getcwd()
file_error = '文件丢失，请重新安装'
ok = '安装完成'
install = 'pip install'
i = '-i https://mirrors.aliyun.com/pypi/simple/'
i2 = '安装'

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
def tensorFlow():
    os.system('pip install TensorFlow -i https://mirrors.aliyun.com/pypi/simple/')
    messagebox.showinfo(install, ok)
def pytorch():
    os.system('pip install pytorch -i https://mirrors.aliyun.com/pypi/simple/')
    messagebox.showinfo(install, ok)
def openai():
    os.system('pip install openai -i https://mirrors.aliyun.com/pypi/simple/')
    messagebox.showinfo(install, ok)
def keras():
    os.system('pip install keras -i https://mirrors.aliyun.com/pypi/simple/')
    messagebox.showinfo(install, ok)
def scikit_learn():
    os.system('pip install scikit-learn -i https://mirrors.aliyun.com/pypi/simple/')
    messagebox.showinfo(install, ok)
def lightGBM():
    os.system('pip install lightGBM -i https://mirrors.aliyun.com/pypi/simple/')
    messagebox.showinfo(install, ok)
def CatBoost():
    os.system('pip install CatBoost -i https://mirrors.aliyun.com/pypi/simple/')
    messagebox.showinfo(install,ok)
def pandas():
    os.system(f'pip install pandas {i}')
    messagebox.showinfo(install, ok)
def pyttsx():
    os.system(f'pip install pyttsx {i}')
    messagebox.showinfo(install, ok)
def pylatex():
    os.system(f'pip install pylatex {i}')
    messagebox.showinfo(install , ok)
def XGBoost():
    os.system(f'pip install XGBoost {i}')
    messagebox.showinfo(install ,ok)
def fh():
    root.destroy()

# Button
bt_tensorFlow = Button(frame, text='TensorFlow安装', command=tensorFlow)
bt_palatex = Button(frame, text=0)
bt_pytorch = Button(frame, text='pytorch安装', command=pytorch)
bt_keras = Button(frame, text='keras安装', command=keras)
bt_lightGBM = Button(frame, text='lightGBM安装', command=lightGBM)
bt_pandas = Button(frame, text='pandas安装', command=pandas)
bt_pyttsx = Button(frame, text='pyttsx安装', command=pyttsx)
bt_pylatex = Button(frame, text='pylatex安装', command=pylatex)
bt_scikit_learn = Button(frame, text='scikit-learn安装', command=scikit_learn)
bt_openai = Button(frame, text='openai安装', command=openai)
bt_XGBoost = Button(frame ,text='XGBoost安装', command=XGBoost)
bt_fh = Button(frame, text='返回', command=fh)

# pack
Label(root, text='机器学习类库安装').pack()
bt_fh.pack()
bt_tensorFlow.pack()
bt_pytorch.pack()
bt_keras.pack()
bt_lightGBM.pack()
bt_pandas.pack()
bt_scikit_learn.pack()
bt_XGBoost.pack()
bt_pyttsx.pack()
bt_pylatex.pack()
bt_openai.pack()



# mainloop
root.title('install')
root.geometry('150x150+400+700')
root.mainloop()