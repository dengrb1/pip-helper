import os
import platform
from time import time
import sys

t = 'taskkill -f -t -im '

def Linux():
    system = platform.system()
    if system == 'Linux':
        pass
    elif system == 'Windows':
        os.system(t + 'client.exe')
        os.system()