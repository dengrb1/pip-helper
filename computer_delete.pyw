from pip_helper_ui import ScrollWindow, make_pip_action

ACTIONS = [
    ("TensorFlow删除", ["tensorflow"]),
    ("pytorch删除", ["torch"]),
    ("keras删除", ["keras"]),
    ("lightGBM删除", ["lightgbm"]),
    ("pandas删除", ["pandas"]),
    ("scikit-learn删除", ["scikit-learn"]),
    ("XGBoost删除", ["xgboost"]),
    ("CatBoost删除", ["catboost"]),
    ("pyttsx删除", ["pyttsx"]),
    ("pylatex删除", ["pylatex"]),
    ("openai删除", ["openai"]),
]


def main() -> None:
    window = ScrollWindow(title="delete", geometry="220x320+400+650", header="机器学习类库删除")
    window.add_button("返回", window.root.destroy)
    for label, packages in ACTIONS:
        window.add_button(label, make_pip_action("uninstall", packages, use_mirror=False))
    window.run()


if __name__ == "__main__":
    main()
