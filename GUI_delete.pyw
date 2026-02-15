from pip_helper_ui import ScrollWindow, make_pip_action

ACTIONS = [
    ("pyqt5删除", ["pyqt5", "PyQtWebEngine"]),
    ("wxpython删除", ["wxpython"]),
    ("matplotlib删除", ["matplotlib"]),
    ("seaborn删除", ["seaborn"]),
    ("kivy删除", ["kivy"]),
    ("pyside6删除", ["pyside6"]),
    ("flexx删除", ["flexx"]),
    ("pysimpleGUI删除", ["pysimpleGUI"]),
]


def main() -> None:
    window = ScrollWindow(title="GUI", geometry="220x300+100+100", header="GUI删除")
    window.add_button("返回", window.root.destroy)
    for label, packages in ACTIONS:
        window.add_button(label, make_pip_action("uninstall", packages, use_mirror=False))
    window.run()


if __name__ == "__main__":
    main()
