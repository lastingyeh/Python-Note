import numpy as np

a = np.array([1, 1, 1])
b = np.array([2, 2, 2])

c = np.vstack((a, b))

print('vertical-stack = ', c)
print('a of shape = ', a.shape)
print('c of shape = ', c.shape)

d = np.hstack((a, b))
print('horizontal-stack = ', d)
print('d of shape = ', d.shape)

# it has 3 rows
print('a[:, np.newaxis] = ', a[:, np.newaxis])
# it has 3 cols
print('a[np.newaxis,:] = ', a[np.newaxis, :])

a1 = a[:, np.newaxis]
b1 = b[:, np.newaxis]
# horizontal stack of c1
c1 = np.hstack((a1, b1))

print('c1 = ', c1)

# axis = 0 vertical stack merge
c2 = np.concatenate((a1, b1, b1, a1), axis=1)

print('multiple array stacks', c2)
