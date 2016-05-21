import threading
from time import sleep
from random import random
import logging as log
from Queue import Queue

fmt_str = "%(threadName)s:%(message)s"

log.basicConfig(level=log.DEBUG, format=fmt_str)

def task(delay, condition, q):
    log.debug('waits for notification')
    with condition:
        condition.wait()
        q.put(delay + delay)
        log.debug('quits')
        q.join()

def main():
    ca = threading.Condition()
    q = Queue()

    for i in range(5):
        t = threading.Thread(target=task, args=(random(), ca, q))
        t.start()

    sleep(2)

    with ca:
        ca.notifyAll()

    for i in range(5):
        print(q.get())
        q.task_done()

    print("main thread ends")

if __name__ == '__main__':
    main()


