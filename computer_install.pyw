from pip_helper_ui import ScrollWindow, make_pip_action

ACTIONS = [
    ("TensorFlow安装", ["tensorflow"]),
    ("pytorch安装", ["torch"]),
    ("keras安装", ["keras"]),
    ("lightGBM安装", ["lightgbm"]),
    ("pandas安装", ["pandas"]),
    ("scikit-learn安装", ["scikit-learn"]),
    ("XGBoost安装", ["xgboost"]),
    ("CatBoost安装", ["catboost"]),
    ("pyttsx安装", ["pyttsx"]),
    ("pylatex安装", ["pylatex"]),
    ("openai安装", ["openai"]),
]


def main() -> None:
    window = ScrollWindow(title="install", geometry="220x320+400+700", header="机器学习类库安装")
    window.add_button("返回", window.root.destroy)
    for label, packages in ACTIONS:
        window.add_button(label, make_pip_action("install", packages))
    window.run()


if __name__ == "__main__":
    main()
