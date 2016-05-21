import multiprocessing
from os import getpid

def worrker():
    p_name = multiprocessing.current_process().name
    print "{}: {}".format(p_name, getpid())

def main():
    for i in range(5):
        p = multiprocessing.Process(target=worrker)
        p.start()

    for p in multiprocessing.active_children():
        p.join()

    print("main process ends...")


if __name__ == '__main__':
    main()