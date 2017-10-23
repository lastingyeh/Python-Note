a = [1, 2, 3, 4, 5]

a.insert(1, 6)
a.append(6)
a.remove(1)  # remove first-find()

print('list a', a)
print('last index value', a[-1])
print('range-value', a[1:3])
print('index-value search', a.index(6))
print('count value', a.count(6))
print('sort', a.sort())
print('sorted list a', a)