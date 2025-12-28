#TODO Class and Objects

# Definition of Class
class Car:

    # Constructor: For initialiaing the attributes
    # Invoked immediately whenever object is created.
    def __init__(self, brand, model):

        # Instance Variables
        self.brand = brand
        self.model = model

    # Instance Method
    def full_name(self):
        return f"{self.brand}: {self.model}"

# Creating an object
my_car = Car("Bugatti", "Tourbillon")

# Calling instance method of class car.
print(my_car.full_name())

