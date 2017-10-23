from copy import copy, deepcopy

# as the same ref by 'b = a'
# test by id(p)

a = [1, 2, 3]
b = a

print('b = a', id(b) == id(a))

# as different ref by c,a
c = copy(a)

print('c = a', id(c) == id(a))

c[0] = 4

print('a', a)
print('c', c)

# but as nested list (or object)
d = [1, 2, 3, [4, 5]]

e = copy(d)

print('d == e', id(d) == id(e))

# but as the same ref by d[3],e[3]
print('d[3] == e[3]', id(d[3]) == id(e[3]))

# as immutable used,it needs to use 'deepcopy'
f = deepcopy(d)

print('d[3] == f[3]', id(d[3]) == id(f[3]))
