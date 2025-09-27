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


"""
5th function for numpy is ---- random.reshape
syntax --- numpy.reshape(array, new_shape)
            # OR (as a method)
           array.reshape(new_shape)

defination --  numpy.reshape() is used to change the shape (dimensions) of an existing NumPy array without changing its data.
               It allows you to convert a 1D array into 2D or 3D, or change rows & columns — as long as the total number of elements remains the same.

Example -- import numpy as np

arr = np.arange(6)           # [0 1 2 3 4 5]

new_arr = np.reshape(arr, (2, 3))    # Using function
# Output:
# [[0 1 2]
#  [3 4 5]]

new_arr2 = arr.reshape(3, 2)         # Using method
# Output:
# [[0 1]
#  [2 3]
#  [4 5]]

"""



"""
6th function for numpy is ---- shape
syntax --- array.shape

defination --  shape is an attribute of a NumPy array that returns the dimensions of the array in the form of a tuple.
It tells you how many rows and columns (or higher dimensions) an array has.

Example -- import numpy as np

arr1 = np.array([1, 2, 3, 4])
print(arr1.shape)    # Output: (4,) → 1D array with 4 elements

arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print(arr2.shape)    # Output: (2, 3) → 2 rows, 3 columns

arr3 = np.zeros((2, 3, 4))   # 3D array
print(arr3.shape)    # Output: (2, 3, 4)


"""


"""
7th function for numpy is ---- .eye
syntax --- numpy.eye(N, M=None, k=0, dtype=float)

defination --  numpy.eye() is used to create a 2D array with ones on the main diagonal and zeros elsewhere.

This is commonly known as an identity matrix, which is very useful in linear algebra and matrix operations.

Example -- import numpy as np

np.eye(3)          
# Output:
# [[1. 0. 0.]
#  [1. 1. 0.]
#  [1. 1. 1.]]

np.eye(3, 4)       
# 3 rows, 4 columns

np.eye(4, k=1)     
# Diagonal shifted one position above the main

np.eye(4, k=-1)    
# Diagonal shifted one position below the main

"""



"""
8th function for numpy is ---- .ones
syntax --- numpy.ones(shape, dtype=float)

defination --  numpy.ones() is used to create a new array filled with all ones.
You can specify the shape (dimensions) and data type of the array.

This function is useful when initializing matrices or arrays for operations like weights, placeholders, or default values.

Example -- import numpy as np

np.ones(4)          # Output: [1. 1. 1. 1.]

np.ones((2, 3))     
# Output:
# [[1. 1. 1.]
#  [1. 1. 1.]]

np.ones((2, 3), dtype=int)
# Output:
# [[1 1 1]
#  [1 1 1]]


"""




"""
9th function for numpy is ---- .zeros
syntax --- numpy.zeros(shape, dtype=float)

defination --  numpy.zeros() is used to create a new array filled entirely with zeros.

It is commonly used when you need an empty structure to fill later, like initializing matrices, placeholders, or preparing arrays for calculations.

Example -- import numpy as np

np.zeros(5)           
# Output: [0. 0. 0. 0. 0.]

np.zeros((2, 3))      
# Output:
# [[0. 0. 0.]
#  [0. 0. 0.]]

np.zeros((3, 3), dtype=int)
# Output:
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]]

"""