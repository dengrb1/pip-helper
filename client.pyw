from pip_helper_ui import ScrollWindow, open_exe


def main() -> None:
    window = ScrollWindow(title="选择", geometry="220x230+400+400", header="pip_helper")

    window.add_button("安装模式", lambda: open_exe("install"))
    window.add_button("删除模式", lambda: open_exe("delete"))
    window.add_button("更新日志", lambda: open_exe("update"))
    window.add_button("退出", window.root.destroy)
    window.add_blank_line()
    window.add_button("version 1.7 @2023-2024 dengrb1", lambda: None)

    window.run()


if __name__ == "__main__":
    main()
