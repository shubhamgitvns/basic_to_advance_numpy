import numpy as np

marks = np.array([
    [80, 85, 90],
    [70, 75, 65],
    [92, 88, 95]
])
 # callculate mean as column wise
print(np.mean(marks, axis=0))

 # callculate mean as row wise
print(np.mean(marks, axis= 1))
