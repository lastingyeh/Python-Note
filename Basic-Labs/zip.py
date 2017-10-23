# zip
a = [1, 2, 3]
b = [4, 5, 6, 7]

z = list(zip(a, b))

print(z)

for i, j in zip(a, b):
    print(i, j)

# lambda return simple function
fs = lambda x, y, s: (x + y) / s

print('lambda', fs(6, 3, 3))


# map
def func(x, y):
    return x + y


print(map(func, [1], [2]))
print(map(func, [1, 3], [5, 7]))

m = map(func, [1, 2, 3], [4, 5, 6])

print('m', m)
