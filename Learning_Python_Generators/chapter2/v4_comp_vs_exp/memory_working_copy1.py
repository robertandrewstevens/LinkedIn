import sys

doubles_lc = [num * 2 for num in range(1, 5000)]
doubles_ge = (num * 2 for num in range(1, 5000))

print(sys.getsizeof(doubles_lc))
print(sys.getsizeof(doubles_ge))