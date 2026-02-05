from pip_helper_ui import ScrollWindow, make_pip_action

ACTIONS = [
    ("Numpy删除", ["numpy"]),
    ("scipy删除", ["scipy"]),
    ("sympy删除", ["sympy"]),
    ("pandas删除", ["pandas"]),
    ("pyomo删除", ["pyomo"]),
    ("gpy删除", ["gpy"]),
    ("pydy删除", ["pydy"]),
]


def main() -> None:
    window = ScrollWindow(title="删除", geometry="220x260+400+100", header="计算类删除")
    window.add_button("返回", window.root.destroy)
    for label, packages in ACTIONS:
        window.add_button(label, make_pip_action("uninstall", packages, use_mirror=False))
    window.run()


if __name__ == "__main__":
    main()
