class Car():
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        return self.name.title() + ' ' + self.model.title() + ' ' + str(self.year)

    def set_name(self, name):
        self.name = name
    
    def set_year(self, year):
        self.year = year
    
    def set_model(self, model):
        self.model = model

# Inhearitance
class Battery():
    def __init__(self, battery = 70):
        self.battery = battery
    
    def get_battery_details(self):
        return str(self.battery) + '-kwh'

class ElectricCar(Car):
    def __init__(self, name, model, year):
        super().__init__(name, model, year)
        self.battery = Battery(100)

car_1 = ElectricCar('Tesla', 'Model X', 2020)
print(car_1.get_descriptive_name())
print('Battery power is: ' + car_1.battery.get_battery_details())