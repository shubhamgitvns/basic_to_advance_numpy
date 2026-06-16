"""
  .ravel() -> view
  .flatten() -> copy
  both mathed convert the multy dimmensional array in 1 dimmensional but differnt approch
"""

import numpy as np

arry_2d = np.array([[1,2,3,4],[4,3,2,1]])

print(arry_2d.ravel())
print(arry_2d.flatten())