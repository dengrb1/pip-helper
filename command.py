import subprocess
import time


def run(count: int = 4) -> None:
    for _ in range(count):
        subprocess.Popen(["powershell"], shell=True)


def main() -> None:
    print("正在启动")
    time.sleep(0.66)
    print("Starting up")
    time.sleep(0.22)
    run()


if __name__ == "__main__":
    main()
