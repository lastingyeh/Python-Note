import multiprocessing as mp


def job(x):
	return x * x


def multi_core():
	pool = mp.Pool()
	# 自動分配 處理事件到多核心ＣＰＵ
	res = pool.map(job, range(10))
	print(res)

	res = pool.apply_async(job, (2,))
	print(res.get())

	multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
	print([res.get() for res in multi_res])


if __name__ == '__main__':
	multi_core()
