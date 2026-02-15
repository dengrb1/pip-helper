from pip_helper_ui import ScrollWindow, make_pip_action

ACTIONS = [
    ("pyqt5安装", ["pyqt5", "PyQtWebEngine"]),
    ("wxpython安装", ["wxpython"]),
    ("matplotlib安装", ["matplotlib"]),
    ("seaborn安装", ["seaborn"]),
    ("kivy安装", ["kivy"]),
    ("pyside6安装", ["pyside6"]),
    ("flexx安装", ["flexx"]),
    ("pysimpleGUI安装", ["pysimpleGUI"]),
]


def main() -> None:
    window = ScrollWindow(title="GUI", geometry="220x280+100+110", header="GUI")
    window.add_button("返回", window.root.destroy)
    for label, packages in ACTIONS:
        window.add_button(label, make_pip_action("install", packages))
    window.run()


if __name__ == "__main__":
    main()
