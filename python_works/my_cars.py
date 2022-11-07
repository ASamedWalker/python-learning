from car import Car
from electric_cars import ElectricCar as EC #using aliases

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())


my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())


# import car

# or

# from car import *: Not recommended


# my_beetle = car.Car('volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())

# my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
# print(my_beetle.get_descriptive_name())