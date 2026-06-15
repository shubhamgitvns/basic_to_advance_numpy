import numpy as np

# shape of array
marks = np.array([
    [80, 85, 90],
    [70, 75, 65],
    [92, 88, 95]
])
print("Shape of array",marks.shape)

# Size of array
array = np.array([[1,2,3,4], [1,2,3,4]])
print("Size of array",array.size)

# ndim of array

values = np.array([[
    [80, 85, 90],
    [70, 75, 65],
    [92, 88, 95],
    [98, 34, 99]

]])
print("ndim of array =", values.ndim)
print("ndim of array =", array.ndim)
print(values.shape)

# types of array

print(values.dtype)


# astype covert the type of data type

arry = np.array([1,2,3.9,4.7,9])
int_array = arry.astype(int)
print(int_array.dtype)