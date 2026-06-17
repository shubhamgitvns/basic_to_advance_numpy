"""
np.delete(array_name, index, axis = none)

remove or delete the element in the array

"""

import numpy as np

# delet for 1D array
arry = np.array([10,20,30,40,50])
new_arry = np.delete(arry, len(arry)-2)

print(new_arry)


# delete for 2D array

array_2d = np.array([[1,2,3], [4,5,6]])

new_2d_array_row = np.delete(array_2d, 0, axis=0) # delet the row 
print(new_2d_array_row)

"""
np.delete(array_name, index, axis = none)

remove or delete the element in the array

"""

import numpy as np

# delet for 1D array
arry = np.array([10,20,30,40,50])
new_arry = np.delete(arry, len(arry)-2)

print(new_arry)


# delete for 2D array

array_2d = np.array([[1,2,3], [4,5,6]])

new_2d_array_row = np.delete(array_2d, 0, axis=0) # delet the row 
print(new_2d_array_row)

new_2d_array_colm = np.delete(array_2d, 0, axis=1) # delet the colmn 
print(new_2d_array_colm)

