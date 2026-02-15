"""更新日志页面。"""

import webbrowser
from tkinter import BOTH, END, RIGHT, Button, Label, Tk
from tkinter.scrolledtext import ScrolledText

from pip_helper_ui import make_pip_action

CHANGELOG = """当前版本:1.7 (Not beta or demo)

1.7 加入pygithub库；加入更多的机器学习库,修复一些BUG
1.6 加入更多处理数据库；修复一些BUG；加入WIFI检测；修改更新日志文本放置的位置；加入更新pip包管理工具......
1.5.1 修改pip源，让下载速度变得更加快速！！
1.5 加入更多机器学习库；修复一些BUG;修改pip安装检测代
1.4 加入pip安装检测；加入更多web类库；修复一些BUG
1.3 加入更多GUI库，比如：pyside6, kivy等等；修复一些BUG
1.2.1 加入机器学习库——openai；修复BUG;一键安装所有库正在试验中......
1.2 加入更多可视化库，都在gui安装和删除类里面；修复一些BUG
1.1 加入机器学习库安装；修复BUG；删除“关于”模块
1.0 正式版本。修复BUG；改正更新日志显示问题
0.1.0 暂无日志
"""


def main() -> None:
    root = Tk()
    root.title("更新日志")
    root.geometry("420x320+400+400")

    Button(root, text="在线更新", command=lambda: webbrowser.open("https://kgithub.com/dengrb1/pip-helper")).pack(side=RIGHT)
    Button(root, text="pip包更新", command=make_pip_action("install", ["--upgrade", "pip"])).pack(side=RIGHT)
    Button(root, text="返回", command=root.destroy).pack(side=RIGHT)

    Label(root, text="更新日志").pack()

    text_box = ScrolledText(root)
    text_box.pack(fill=BOTH, expand=True)
    text_box.insert(END, CHANGELOG)
    text_box.configure(state="disabled")

    root.mainloop()


if __name__ == "__main__":
    main()
