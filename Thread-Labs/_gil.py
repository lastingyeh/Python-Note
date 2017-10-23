import threading
from queue import Queue
import copy
import time


# https://github.com/MorvanZhou/tutorials/blob/master/threadingTUT/thread5_GIL.py

def job(l, q):
    res = sum(l)
    q.put(res)


def multi_threading(l):
    q = Queue()
    threads = []

    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
        t.start()
        threads.append(t)

    [t.join() for t in threads]

    total = 0
    for _ in range(4):
        total += q.get()

    print(total)


def normal(l):
    total = sum(l)
    print(total)


if __name__ == '__main__':
    data = list(range(1000000))
    # print(len(data))

    # normal run single-threading
    s_t = time.time()
    normal(data * 4)
    print('normal: ', time.time() - s_t)

    # multi-threading
    s_t = time.time()
    multi_threading(data)
    print('multi-threading: ', time.time() - s_t)
