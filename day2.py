import numpy as np
import time

#  a simplified version of code to know the time taken by array and list

t1 = time.time()
list = [1,2,3,4,5]
t2 = time.time()
tl = t2 - t1
print("list time :",tl)

t3 = time.time()
arr = np.array([1,2,3,4,5])
t4 = time.time()
ta = t4 - t3
print("array time :",ta)

# %%
"""

1. For small datasets, Python lists often perform faster in creation time because
   NumPy has setup overhead.

2. For large datasets (thousands, millions, or more), NumPy arrays are much faster
   for computation and memory efficiency because:

   -- Operations are done in compiled C code.
   -- Memory is contiguous, which improves CPU cache efficiency.

"""
# %%



