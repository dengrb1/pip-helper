from pip_helper_ui import ScrollWindow, make_pip_action

ACTIONS = [
    ("pygame安装", ["pygame"]),
    ("pyopenGL安装", ["pyopengl"]),
    ("pyglet安装", ["pyglet"]),
    ("pyode安装", ["pyode"]),
    ("panda3d安装", ["panda3d"]),
    ("cocos2d安装", ["cocos2d"]),
    ("kivy安装", ["kivy"]),
    ("arcade安装", ["arcade"]),
]


def main() -> None:
    window = ScrollWindow(title="game", geometry="220x320+100+80", header="游戏库安装")
    window.add_button("返回", window.root.destroy)
    for label, packages in ACTIONS:
        window.add_button(label, make_pip_action("install", packages))
    window.run()


if __name__ == "__main__":
    main()
