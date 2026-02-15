from pip_helper_ui import ScrollWindow, make_pip_action

ACTIONS = [
    ("Requests安装", ["requests"]),
    ("django安装", ["django"]),
    ("fastAPI安装", ["fastapi"]),
    ("sanic安装", ["sanic"]),
    ("nameko安装", ["nameko"]),
    ("pydantic安装", ["pydantic"]),
]


def main() -> None:
    window = ScrollWindow(title="web", geometry="220x280+600+400", header="web类安装")
    window.add_button("返回", window.root.destroy)
    for label, packages in ACTIONS:
        window.add_button(label, make_pip_action("install", packages))
    window.run()


if __name__ == "__main__":
    main()
