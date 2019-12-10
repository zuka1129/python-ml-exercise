import threading
import time
import random

num = 10000


def my_print(info):
    # time.sleep(random.randint(1,10))
    print("执行事件" + info)
    global num
    num = num - 1
    print(num)
if __name__ == "__main__":
    t1 = threading.Thread(target=my_print, args=("线程1", ))
    t2 = threading.Thread(target=my_print, args=("线程2", ))
    t3 = threading.Thread(target=my_print, args=("线程3", ))
    t4 = threading.Thread(target=my_print, args=("线程4", ))
    t5 = threading.Thread(target=my_print, args=("线程5", ))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    print("do something")
