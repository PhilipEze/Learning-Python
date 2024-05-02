weight = 41.5
premium_ground_price = 125.00


#Ground shipping
if weight <= 2:
  ground_cost =1.50*weight+20
elif weight <= 6:
  ground_cost =3.00*weight+20
elif weight <= 10:
  ground_cost =4.00*weight+20
elif weight > 10:
  ground_cost =4.75*weight+20
else:
  print("Error")  
print("Ground Shipping cost = $"+str(ground_cost))


#Ground Premium Shipping Cost
print(50*"*")
print("Ground Shipping Premium cost = $"+str(premium_ground_price))

#Drone shipping
if weight <= 2:
  ground_cost =4.50*weight
elif weight <= 6:
  ground_cost =9.00*weight
elif weight <= 10:
  ground_cost =12.00*weight
elif weight > 10:
  ground_cost =14.25*weight
else:
  print("Error")
print(50*"*")  
print("Drone Shipping cost = $"+str(round(ground_cost,2)))



# Cheapest method to ship --> 4.8lb is Ground Shipping.
# Cheapest method to ship --> 41.5lb is Ground Shipping Premium.
