from pip_helper_ui import ScrollWindow, make_pip_action

ACTIONS = [
    ("pygame删除", ["pygame"]),
    ("pyopenGL删除", ["pyopengl"]),
    ("pyglet删除", ["pyglet"]),
    ("pyode删除", ["pyode"]),
    ("panda3d删除", ["panda3d"]),
    ("cocos2d删除", ["cocos2d"]),
    ("kivy删除", ["kivy"]),
    ("arcade删除", ["arcade"]),
]


def main() -> None:
    window = ScrollWindow(title="game", geometry="220x320+100+40", header="游戏库删除")
    window.add_button("返回", window.root.destroy)
    for label, packages in ACTIONS:
        window.add_button(label, make_pip_action("uninstall", packages, use_mirror=False))
    window.run()


if __name__ == "__main__":
    main()
