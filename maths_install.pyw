from pip_helper_ui import ScrollWindow, make_pip_action

ACTIONS = [
    ("Numpy安装", ["numpy"]),
    ("scipy安装", ["scipy"]),
    ("sympy安装", ["sympy"]),
    ("pandas安装", ["pandas"]),
    ("pyomo安装", ["pyomo"]),
    ("gpy安装", ["gpy"]),
    ("pydy安装", ["pydy"]),
]


def main() -> None:
    window = ScrollWindow(title="install", geometry="220x260+10+100", header="计算类安装")
    window.add_button("返回", window.root.destroy)
    for label, packages in ACTIONS:
        window.add_button(label, make_pip_action("install", packages))
    window.run()


if __name__ == "__main__":
    main()
