import multiprocessing as mp

# https://docs.python.org/3/library/array.html
# double
value = mp.Value('d', 1)
# int of array
value = mp.Array('i', [1, 2, 3])
