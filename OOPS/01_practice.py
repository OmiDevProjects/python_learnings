class Car:

    total_car = 0

    def __init__(self, brand=None, model=None):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def get_full_name(self):
        return f'Brand: {self.__brand}, Model: {self.__model}'

    def fuel_type(self):
        return 'Petrol or Disel'

    @property
    def model(self):
        return self.__model

    @staticmethod
    def general_information():
        return f'Car is a mode of transport with lots of rules and regulations. Use it in a kind way'


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def get_full_name(self):
        return f'EV :: Brand: {self.get_brand()}, Model: {self.get_model()}, Battery Size: {self.battery_size}'

    def fuel_type(self):
        return 'Electric Charge'


toyota = Car('Toyota', 'Corolla')
print(toyota.get_full_name())

# toyota.set_model('ABC')
print(toyota.model)
print(toyota.fuel_type())

tesla = ElectricCar('Tesla', 'Boomer', '85kWH')
print(tesla.get_full_name())
print(tesla.fuel_type())

print(Car.total_car)

print(Car.general_information())
print(ElectricCar.general_information())