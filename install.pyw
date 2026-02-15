from pip_helper_ui import ScrollWindow, make_pip_action, open_exe


def main() -> None:
    window = ScrollWindow(title="安装", geometry="220x320+100+50", header="安装列表")

    window.add_button("返回", window.root.destroy)
    window.add_button("GUI类安装", lambda: open_exe("GUI_install"))
    window.add_button("web类安装", lambda: open_exe("web_install"))
    window.add_button("机器学习类库安装", lambda: open_exe("computer_install"))
    window.add_button("maths类安装", lambda: open_exe("maths_install"))
    window.add_button("game类安装", lambda: open_exe("game_install"))
    window.add_blank_line()

    quick_packages = [
        ("pyinstaller安装", ["pyinstaller"]),
        ("tqdm安装", ["tqdm"]),
        ("pygithub安装", ["pygithub"]),
        ("nuitka安装", ["nuitka"]),
        ("pywin32安装", ["pywin32"]),
    ]
    for label, packages in quick_packages:
        window.add_button(label, make_pip_action("install", packages))

    window.run()


if __name__ == "__main__":
    main()
