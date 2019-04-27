# this defines the total number of cars
cars = 100
# this defines the space in each car
space_in_a_car = 4.0
# this defines the number of drivers
drivers = 30
# this defines the number of passengers
passengers = 90
# this relates the number of cars and drivers to find the number of undriven cars
cars_not_driven = cars - drivers
# this defines the number of driven cars as the number of drivers
cars_driven = drivers
# this relates the total number of space avialable among all the cars
carpool_capacity = cars_driven * space_in_a_car
# this finds how many people need to go in each car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "we have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
print "Hey %s there." % "you"