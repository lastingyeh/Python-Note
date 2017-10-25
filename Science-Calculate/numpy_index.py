import numpy as np

a = np.arange(3, 15)

print(a)
print('a[3] = ', a[3])

b = np.arange(3, 15).reshape((3, 4))

print('b = ', b)
print('b[2] = ', b[2])
print('b[1][1] = ', b[1][1])
print('b[2][1] = ', b[2][1], b[2, 1])
# r3 all-cols
print('b[2,:]', b[2, :])
# r2,c1
print('b[1,1:2] = ', b[1, 1:2])
# r2,c1-c2
print('b[1,1:3] = ', b[1, 1:3])

# for loop
# print rows
for row in b:
	print('row = ', row)

# matrix transpose
print('b.T = ', b.T)
# print columns
for col in b.T:
	print('column', col)

# loop each
print('flatten =', b.flatten())

for item in b.flat:
	print('item = ', item)
