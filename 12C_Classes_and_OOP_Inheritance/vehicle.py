# vehicle.py
# The class definitions for a vehicle, a car, and a bus

class Vehicle:  # Superclass
    def __init__(self, license):
        self.license = license  # License plate

    def get_license(self):
        info = 'License Plate: '+self.license
        return info

class Car(Vehicle):  # Subclass. Will inherit all attributes of Vehicle.
    def __init__(self, license, make, model):  # Override __init__
        super().__init__(license)
        self.make = make
        self.model = model

    def get_car_info(self):
        info = 'Make: '+self.make+', Model: '+self.model
        return info

class Bus(Vehicle):  # Another subclass
    def __init__(self, license, capacity):
        super().__init__(license)
        self.capacity = capacity  # Number of passengers

    def get_bus_info(self):
        info = 'Capacity: '+str(self.capacity)
        return info