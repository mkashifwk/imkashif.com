import os
import threading




def setInterval(func, sec):
    def func_wrapper():
        setInterval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def gitPull():
	print('git pull')
	os.system('git pull')

setInterval(gitPull , 5)