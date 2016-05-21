import threading
from time import sleep
from random import random
import logging as log

fmt_str = "%(threadName)s:%(message)s"

log.basicConfig(level=log.DEBUG, format=fmt_str)

def task(delay, lock):
    t_id = threading.currentThread().ident
    t_name = threading.currentThread().getName()
    log.debug('waits for lock')
    with lock:
        log.debug('acquired lock')
        sleep(delay)
        print "{}: {}".format(t_id, t_name)
        log.debug('release lock')

def main():
    #mutex using Lock object
    #lock = threading.Lock()
    #mutex using Semaphore object
    lock = threading.Semaphore(1)
    for i in range(5):
        t = threading.Thread(target=task, args=(random(), lock))
        t.start()

    for t in threading.enumerate():
        if t is not threading.currentThread():
            t.join()

    print("main thread ends")

if __name__ == '__main__':
    main()


