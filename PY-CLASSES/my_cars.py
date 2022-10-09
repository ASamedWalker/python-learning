# from car import Car, ElectricCar
# import car
from car import Car
from electric_car import ElectricCar as EC

# my_beetle = Car('volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())


# my_tesla = ElectricCar('tesla', 'roadster', 2019)
# print(my_tesla.get_descriptive_name())

# my_beetle = car.Car('volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())


# my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
# print(my_tesla.get_descriptive_name())

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())


my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())