import multiprocessing as mp
import threading as td
import time


def job(q):
	res = 0
	for i in range(1000000):
		res += i + i ** 2 + i ** 3
	q.put(res)


def normal():
	res = 0
	for _ in range(2):
		for i in range(1000000):
			res += i + i ** 2 + i ** 3
	print('normal:', res)


def multi_process():
	q = mp.Queue()
	p1 = mp.Process(target=job, args=(q,))
	p2 = mp.Process(target=job, args=(q,))

	p1.start()
	p2.start()

	p1.join()
	p2.join()

	res1 = q.get()
	res2 = q.get()

	print('multi-process', res1 + res2)


def multi_thread():
	q = mp.Queue()
	t1 = td.Thread(target=job, args=(q,))
	t2 = td.Thread(target=job, args=(q,))

	t1.start()
	t2.start()

	t1.join()
	t2.join()

	res1 = q.get()
	res2 = q.get()

	print('multi-thread', res1 + res2)


# 操作方式與 threading 相同
if __name__ == '__main__':
	st = time.time()
	normal()
	st1 = time.time()
	print('normal time:', st1 - st)
	multi_process()
	st2 = time.time()
	print('multi-process', st2 - st1)
	multi_thread()
	st3 = time.time()
	print('multi-thread', st3 - st2)
