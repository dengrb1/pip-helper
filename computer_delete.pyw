from tkinter import *
from tkinter import messagebox
import os


root = Tk()
ml = os.getcwd()
file_error = '文件丢失，请重新安装'
uninstall = 'pip uninstall'
ok = '删除完成'


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
def TensorFlow():
    os.system('pip uninstall TensorFlow')
    messagebox.showinfo(uninstall, ok)
def pytorch():
    os.system('pip uninstall pytorch')
    messagebox.showinfo(uninstall, ok)
def openai():
    os.system('pip uninstall openai')
    messagebox.showinfo(uninstall, ok)
def keras():
    os.system('pip uninstall keras')
    messagebox.showinfo(uninstall, ok)
def scikit_learn():
    os.system('pip uninstall scikit-learn')
    messagebox.showinfo(uninstall, ok)
def lightGBM():
    os.system('pip uninstall lightGBM')
    messagebox.showinfo(uninstall, ok)
def CatBoost():
    os.system('pip uninstall CatBoost')
    messagebox.showinfo(uninstall, ok)
def XGBoost():
    os.system('pip uninstall XGBoost')
    messagebox.showinfo(uninstall, ok)
def fh():
    root.destroy()

# Button
bt_TensorFlow = Button(frame, text='TensorFlow删除', command=TensorFlow)
bt_pytorch = Button(frame, text='pytorch删除', command=pytorch)
bt_keras = Button(frame, text='keras安装', command=keras)
bt_lightGBM = Button(frame, text='lightGBM安装', command=lightGBM)
bt_scikit_learn = Button(frame, text='scikit-learn安装', command=scikit_learn)
bt_XGBoost = Button(frame, text='XGBoost删除', command=XGBoost)
bt_openai = Button(frame, text='openai删除', command=openai)
bt_fh = Button(frame, text='返回', command=fh)

# pack
Label(root, text='机器学习类库删除').pack()
bt_TensorFlow.pack()
bt_pytorch.pack()
bt_keras.pack()
bt_lightGBM.pack()
bt_XGBoost.pack()
bt_scikit_learn.pack()
bt_openai.pack()
bt_fh.pack()


# mainloop
root.title('delete')
root.geometry('150x150+400+650')
root.mainloop()