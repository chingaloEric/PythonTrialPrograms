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
class ElectricCar(Car):
    def __init__(self, name, model, year):
        super().__init__(name, model, year)

car_1 = ElectricCar('Tesla', 'Model X', 2020)
print(car_1.get_descriptive_name())