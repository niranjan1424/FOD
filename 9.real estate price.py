import pandas as pd
data = {
    "property ID " :[123,321,332,619,335],
    "location" :["chennai","tambaram","akm","boatclub","akm"],
    "bedrooms" :[4,5,6,4,5],
    "no of sq feet " :[1200,2300,2500,2800,1800],
    "price" :[100000,200000,300000,450000,350000]
    }
property_data=pd.DataFrame(data)
print(property_data)
avg_price = property_data.groupby("location")["price"].mean()
print("avg price of property in each location \n",avg_price)
property_morethan_4_bedrooms =len(property_data[property_data["bedrooms"]>4])
print("no of property with more than 4 bedroooms =",property_morethan_4_bedrooms)

