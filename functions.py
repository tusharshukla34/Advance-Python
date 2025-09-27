import numpy as np


"------------------------         Numpy library functions                 ------------------"
"""
1st function for numpy is ---- arange
syntax --- numpy.arange(start, stop, step, dtype=None)
defination -- numpy.arange() is a function used to create arrays with evenly spaced values within a given range. It works similar to Python's built-in range() function but returns a NumPy array instead of a list — making it more efficient for numerical and scientific operations.

Example -- import numpy as np

arr1 = np.arange(5)          # Output: [0 1 2 3 4]
arr2 = np.arange(2, 10, 2)   # Output: [2 4 6 8]
arr3 = np.arange(0, 1, 0.2)  # Output: [0.  0.2 0.4 0.6 0.8]

"""
x = np.arange(1,6)
print(x)

# one more thing what is the difference when we print x and print(x) check

"""
2nd function for numpy is ---- linspace
syntax --- numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
defination -- numpy.linspace() is used to generate an array of evenly spaced numbers over a specified interval. Unlike arange(), which uses a step size, linspace() lets you specify the number of values you want between the start and end.


Example -- import numpy as np

arr1 = np.linspace(0, 10, 5)          # Output: [ 0.   2.5  5.   7.5 10. ]
arr2 = np.linspace(1, 2, 4, endpoint=False)  # Output: [1.   1.25 1.5  1.75]
arr3 = np.linspace(0, 1, 5, retstep=True)    # Output: (array([...]), step_size)

"""

x = np.linspace(1,5)
print(x)

"""
3rd function for numpy is ---- random.randient
syntax --- numpy.random.randint(low, high=None, size=None, dtype=int, endpoint=False)

defination -- numpy.random.randint() is used to generate random integers within a specified range.
It can return a single integer or an array of integers depending on the size parameter.

Example -- import numpy as np

np.random.randint(10)            # Output: random int from 0 to 9
np.random.randint(5, 15)         # Output: random int from 5 to 14
np.random.randint(1, 10, size=5) # Output: [3 8 1 6 9]
np.random.randint(1, 10, size=(2,3)) # 2x3 matrix of random ints

"""

x = np.random.randint(1,6)
print(x)


"""
4th function for numpy is ---- random.rand
syntax --- numpy.random.rand(d0, d1, d2, ...)

defination --  numpy.random.rand() is used to generate an array of random numbers drawn from a uniform distribution between 0 and 1.

Example -- import numpy as np

np.random.rand()          # Output: e.g. 0.3748 (single random float)
np.random.rand(3)         # Output: [0.12 0.87 0.45] (1D array)
np.random.rand(2, 3)      # Output: 2x3 matrix with random floats

"""

x = np.random.rand(1,4,4)
print(x)
