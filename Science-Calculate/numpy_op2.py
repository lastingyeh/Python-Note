import numpy as np

a = np.arange(14, 2, -1).reshape((3, 4))
print('a', a)

print('min-index', np.argmin(a))
print('max-index', np.argmax(a))

# average op
print('mean', np.mean(a), a.mean())
print('average', np.average(a))

# median
print('median', np.median(a))

# cumulative-sum
print('cum-sum', np.cumsum(a))

# diff
print('diff', np.diff(a))

# non-zero
# r0 c0 > non-zero ...etc
print('non-zero', np.nonzero(a))

# sort (sort by single column)
print('sort', np.sort(a))

# reverse matrix ((4,3) > (3,4))
print('transpose', np.transpose(a))

# clip (< 5 = 5,> 9 = 9)
print('clip', np.clip(a, 5, 9))
