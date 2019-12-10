from threading import Thread
import threading
import time
class Boss(Thread):
    def run(self):
        print('infomation one')
        print(events.isSet())
        events.set()
        time.sleep(2)
        print('information two')
        print(events.isSet())
        events.set()
class Worker(Thread):
    def run(self):
        events.wait()
        print('information one one')
        events.clear()
        events.wait()
        print('information two two')

if __name__ == '__main__':

    events = threading.Event()
    threads = []
    for i in range(5):
        threads.append(Woker())




