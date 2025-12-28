#TODO: Create an Electric Car class that inherits from the car class and has an addtional attribute barttery_size.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand}: {self.model}"

# Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        # Calling constructor of base class
        super().__init__(brand, model)
        self.battery_size = battery_size

    def battery_info(self):
        # Accessing base class attribute.
        return f"{self.model} has {self.battery_size}."

    def get_brand(self):
        return f'{super().get_brand()}: is the current brand of this {self.model} model.'


# Creating an object of derived class 
my_car = ElectricCar("Bugatti", "Tourbillon", "90KWh")

# Calling base class method
print(my_car.full_name())
print(my_car.battery_info())
print(my_car.get_brand())
