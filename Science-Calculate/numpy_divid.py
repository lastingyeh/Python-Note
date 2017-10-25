import numpy as np

a = np.arange(12).reshape((3, 4))

print('a', a)

# print('split by horizontal divide', np.split(a, 2, axis=1))
# print('split by vertical divide', np.split(a, 3, axis=0))

# 不對等分割
print('not equal split', np.array_split(a, 3, axis=1))

print('vsplit = ', np.vsplit(a, 3))
print('hsplit = ', np.hsplit(a, 2))
