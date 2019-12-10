#线程类测试
# from threading import Thread
# import os
# class Hello(Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#     def run(self):
#         print('hello %s' %self.name)
#         print(os.getpid())

# t = Hello('i am a thread class')
# t.start()
# print(os.getpid())
import threading

num = 100
#线程函数测试
def my_print(info):
    print('excute event'+info)
    global num
    num = num - 1
    print(num)
# for i in range(5):
#     my_print('i')
if __name__ == '__main__':
    t1 = threading.Thread(target=my_print, args=('event1',))
    t2 = threading.Thread(target=my_print, args=('event2',))
    t3 = threading.Thread(target=my_print, args=('event3',))
    t4 = threading.Thread(target=my_print, args=('event4',))
    t5 = threading.Thread(target=my_print, args=('event5',))


    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
