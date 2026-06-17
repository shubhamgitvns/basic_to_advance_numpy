
import numpy as np

arry = np.array([1, 3, np.nan, np.nan, 7, 9, np.nan])

print(np.isnan(arry)) #  return the boolian value

# replace the np.nan value

clean_arry = np.nan_to_num(arry, nan = 10) # defolt 0 value
print(clean_arry)

# handle inf value

infarry = np.array([1, 3, np.inf, np.inf, 7, 9, np.inf])
print(np.isinf(infarry)) 


clean_inf_arry = np.nan_to_num(infarry, posinf= 10, neginf= -10)
print(clean_inf_arry)