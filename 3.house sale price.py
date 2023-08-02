import numpy as np
house_data = np.array([
    [4, 2000, 250000],
    [5, 2400, 300000],
    [3, 1800, 200000],
    [5, 2800, 350000],
])
bedrooms_greater_than_four = house_data[house_data[:, 0] > 4]
print("bedroom",bedrooms_greater_than_four)

