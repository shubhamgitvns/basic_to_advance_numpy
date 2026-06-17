"""
Apply the disscount to each list data avoid using numpy

"""
prices = [100,200,300]
dis = 10
final_prices = []

for price in prices:
    list = price - (price * dis/100)
    final_prices.append(list)

print(final_prices)
