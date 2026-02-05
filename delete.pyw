from pip_helper_ui import ScrollWindow, make_pip_action, open_exe


def main() -> None:
    window = ScrollWindow(title="删除", geometry="220x300+100+10", header="删除模式")

    window.add_button("返回", window.root.destroy)
    window.add_button("GUI类删除", lambda: open_exe("GUI_delete"))
    window.add_button("web类删除", lambda: open_exe("web_delete"))
    window.add_button("机器学习类删除", lambda: open_exe("computer_delete"))
    window.add_button("maths类删除", lambda: open_exe("maths_delete"))
    window.add_button("game类删除", lambda: open_exe("game_delete"))

    quick_packages = [
        ("pyinstaller删除", ["pyinstaller"]),
        ("tqdm删除", ["tqdm"]),
        ("pygithub删除", ["pygithub"]),
        ("nuitka删除", ["nuitka"]),
        ("pywin32删除", ["pywin32"]),
        ("numpy删除", ["numpy"]),
    ]
    for label, packages in quick_packages:
        window.add_button(label, make_pip_action("uninstall", packages, use_mirror=False))

    window.run()


if __name__ == "__main__":
    main()
