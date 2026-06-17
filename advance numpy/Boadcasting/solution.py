
import numpy as np

prices = np.array([100,200,300])
dis = 10

final_prices = prices - (prices * dis/100)
print(final_prices)