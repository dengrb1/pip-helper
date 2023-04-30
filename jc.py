import os
import webbrowser
from time import sleep


error = 0
ok = 0
ml = os.getcwd()


def jc(exe_name):
    if os.path.exists(os.path.join(ml,f"{exe_name}.exe")):
        ok += 1
    else:
        error += 1
        pass
    pass

def client():
    jc("client")
    
def install():
    jc("install")

def delete():
    jc("delete")

def gk():
    jc("gk")

def update():
    jc("update")


# mainloop
client()
install()
delete()
gk()
update()

sleep(0.555)

print(f"共有{ok}个文件正常,有{error}个文件丢失！")
sleep(1)
webbrowser.open("https://github.com/dengrb1/pip-helper")

sleep(5)
exit()
