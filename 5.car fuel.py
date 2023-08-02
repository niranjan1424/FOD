import numpy as np
fuel_efficiency = np.array([[14,16],
                           [15,13],
                           [9,18]
])
avg_fuel =np.mean(fuel_efficiency, axis=0)
print(avg_fuel)
model1_fuel=avg_fuel[0]
model2_fuel=avg_fuel[1]
percentage_increase =( (model2_fuel - model1_fuel)/model1_fuel *100)
print(percentage_increase,"%")
