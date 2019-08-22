cars = 100
space_in_a_car = 4 
drivers = 30
passangers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passangers_per_car = passangers / cars_driven

#one way to write This
print("There are", cars, "cars available.")
#hopefully this is another way to write this
print("There are " + str(cars) + " cars available.")
print("There will be", cars_not_driven, "empty cars is each run.")
print("We can transport", carpool_capacity, "Passangers each run.")
print("We have", passangers, "peaple to transport today.")
print("We need to put", average_passangers_per_car, " passangers in each car.")
