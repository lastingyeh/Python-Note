import multiprocessing as mp
import time


def job(v, num, lock):
	lock.acquire()

	for _ in range(10):
		time.sleep(0.1)
		# 設定取出共享值
		v.value += num
		print(v.value)

	lock.release()


def multi_core():
	lock = mp.Lock()
	# 共享內存值初始
	v = mp.Value('i', 0)

	p1 = mp.Process(target=job, args=(v, 1, lock))
	p2 = mp.Process(target=job, args=(v, 3, lock))

	p1.start()
	p2.start()

	p1.join()
	p2.join()


if __name__ == '__main__':
	multi_core()
