from pip_helper_ui import ScrollWindow, make_pip_action

ACTIONS = [
    ("Requests删除", ["requests"]),
    ("django删除", ["django"]),
    ("fastAPI删除", ["fastapi"]),
    ("sanic删除", ["sanic"]),
    ("nameko删除", ["nameko"]),
    ("pydantic删除", ["pydantic"]),
]


def main() -> None:
    window = ScrollWindow(title="web", geometry="220x260+100+30", header="web类删除")
    window.add_button("返回", window.root.destroy)
    for label, packages in ACTIONS:
        window.add_button(label, make_pip_action("uninstall", packages, use_mirror=False))
    window.run()


if __name__ == "__main__":
    main()
