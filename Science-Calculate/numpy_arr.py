import numpy as np

a = np.array([2, 23, 4], dtype=np.int)

b = np.array([[2, 23, 4], [2, 32, 4]])

# init-value:0 matrix (r:3,c:4)
c = np.zeros((3, 4), dtype=np.int16)

# close to zero-value matrix (r:3,c:4)
d = np.empty((3, 4))

e = np.arange(10, 20, 2)

# (r:3,c:4)
f = np.arange(12).reshape((3, 4))

# between 1 to 10 divide by 6 parts; (r:2,c:3)
g = np.linspace(1, 10, 6).reshape((2, 3))

print(c)
