import multiprocessing as mp


def job(queue, p):
	res = 0
	for i in range(1000):
		res += i + i ** 2 + i ** 3
	print(f'{p} finished,result:{res}')
	queue.put(res)


# 操作方式與 threading 相同
if __name__ == '__main__':
	# 取出計算值 使用Queue
	q = mp.Queue()
	p1 = mp.Process(target=job, args=(q, 'p1'))
	p2 = mp.Process(target=job, args=(q, 'p2'))
	p1.start()
	p1.join()
	p2.start()
	p2.join()

	res1 = q.get()
	res2 = q.get()

	print(res1 + res2)
