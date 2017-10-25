import numpy as np

a = np.array([10, 20, 30, 40])
b = np.arange(4)

# print(a, b)

c = a + b

d = a - b

e = a * b

# 10**0,20**1,30**2,40**3
f = a ** b

g = 10 * np.sin(a)

h = np.tan(a)

# print(g)

# array filter
# print('b < 3', b < 3)
# print('b == 3', b == 3)

# 2-dims op
h = np.array([[1, 1], [0, 1]])

i = np.arange(4).reshape((2, 2))

# print('h', h)
# print('i', i)

j = h * i
# matrix op (k == m)
# https://zh.wikipedia.org/wiki/%E7%9F%A9%E9%99%A3%E4%B9%98%E6%B3%95
k = np.dot(h, i)
m = h.dot(i)

# print('j', j) [[2 4][2 3]]
# print('k', k)
# print('m', m)

# random
# n = np.random.random((2, 4))

n = np.arange(0, 8).reshape((2, 4))

print('n', n)
# print('sum', np.sum(n))
# print('min', np.min(n))
# print('max', np.max(n))

# axis=1 行相加 axis=0 列相加 (min,max 同上）
print('axis 1 sum', np.sum(n, axis=1))
print('axis 1 min', np.min(n, axis=0))
print('axis 1 max', np.max(n, axis=1))
