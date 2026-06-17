"""
Vertical  -> vstack
Horizontal -> hstack
"""

import numpy as np

arr_1 = np.array([1,2,3,4])
arr_2 = np.array([5,6,7,4])

vstack = np.vstack((arr_1, arr_2))  

hstack = np.hstack((arr_1, arr_2))

print(vstack)
print(hstack)