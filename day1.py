#  vs installation was done 

# a = 68
# b = 67
# sum = a +b
# print(a+b)
# print(sum)


# list is fast or array

import numpy as np
import time 

# size = 90000000
# list1 = range(size)
# list2 = range(size)
# start = time.time()
# result = [x+y for x,y in zip(list1,list2)]
# end = time.time()
# print("time taken by list to perform the calculation is :",end - start)

# arr1 = np.arange(size)
# arr2 = np.arange(size)
# start = time.time()
# result = arr1 + arr2
# end = time.time()
# print("time taken by array to perform the calculation is :",end - start)


# another test

# Create a HUGE array (100 million elements)
size = 100000000
arr1 = np.arange(size)
arr2 = np.arange(size)

# Time element-wise addition
start = time.time()
result = arr1 + arr2
end = time.time()
print("Time for adding 100 million numbers:", end - start, "seconds")

# Time element-wise multiplication
start = time.time()
result = arr1 * arr2
end = time.time()
print("Time for multiplying 100 million numbers:", end - start, "seconds")