import numpy as np

a = np.arange(4)

print('a = ', a)

b = a
c = a
d = b

a[0] = 11

# 指向同一位址
print('a,b,c,d = ', a, b, c, d)

print('d[1:3] = ', d[1:3])

# copy array
b = a.copy()

a[0] = 9

print('b = ', b)
