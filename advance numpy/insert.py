"""
insert - add the element in existing array and create the new array for view
np.insert(array, index, value, axis)
axis = 0, row wise
axis = 1 column wise
"""

import numpy as np

arry = np.array([10,20,30,40,50,60])
# inserting the value in new array
new_arry = np.insert(arry, 2, 100 )

print(new_arry)


# 2d array value indexing 

arry_2d = np.array([[1,2], [3,2]])

print(arry)

new_arry_2d = np.insert(arry_2d, 0 , [3,3], axis=0) # add in row 
print(new_arry_2d)


new_arry_2d = np.insert(arry_2d, 0 , [3,3], axis=1) # add in column
print(new_arry_2d)
