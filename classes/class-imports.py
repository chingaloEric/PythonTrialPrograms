from Car import Car, ElectricCar

my_car = Car('Toyota', 'Alphard', 2018)
print(my_car.get_descriptive_name())

my_other_car = ElectricCar('Tesla', 'Cyber trunk', 2022)
print(my_other_car.get_descriptive_name())