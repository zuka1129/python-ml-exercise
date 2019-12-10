#导入进程
from multiprocessing import Process
#导入线程
from threading import Thread
import os
import time
def work():
    print(os.getpid())
#在主进程下开启多个线程
if __name__ == '__main__':
    t1 = Thread(target=work)
    t2 = Thread(target=work)
    t1.start()
    t2.start()
    print('进程---》线程pid', os.getpid())
    #开启多个进程，每个进程有独立pid
    time.sleep(1)
    p1 = Process(target=work)
    p2 = Process(target=work)
    p1.start()
    p2.start()
    print('进程---》线程pid', os.getpid())




