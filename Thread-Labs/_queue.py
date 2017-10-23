import threading
from queue import Queue


def job(l, q):
    for i in range(len(l)):
        l[i] = l[i] ** 2
    q.put(l)


def multi_threading():
    q = Queue()
    threads = []
    data = [[1, 2, 3], [3, 4, 5], [4, 4, 4], [5, 5, 5]]

    # put 4 thread in threads and put result to Queue
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        threads.append(t)

    # await threads finish
    for thread in threads:
        thread.join()

    # from Queue to get results
    results = []
    for _ in range(4):
        results.append(q.get())
    print(results)


if __name__ == '__main__':
    multi_threading()
