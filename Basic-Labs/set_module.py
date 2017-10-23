char_list = ['a', 'b', 'c', 'c', 'd', 'd', 'd']
sentence = 'Welcome Back to This Tutorial'

print(set(sentence))
# remove duplicate value
print(type(set(char_list)))
print(type({'a': 1}))

aSet = set(char_list)
aSet.add('x')

print('aSet', aSet)

# add a > no effect
aSet.add('a')

# remove
print('remove x', aSet.remove('x'))

# discard
print('discard', aSet.discard('y'))

# clear set
aSet.clear()

print('aSet', aSet)

#
set1 = ['a', 'b', 'c', 'd']
set2 = ['b', 'c', 'e', 'f']

print('difference', set(set1).difference(set2))  # ['a','d']
print('intersection', set(set1).intersection(set2))  # ['b','c']
