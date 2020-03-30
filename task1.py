class Car:

    def __init__(self, pax_count, car_mass, gear_count):
        self.pax_count = pax_count
        self.car_mass = car_mass
        self.gear_count = gear_count

    # checking values
    def __setattr__(self, name, value):
        if name == 'pax_count' and (value < 1 or value > 5):
            raise IllegalCarError('car doesn\'t meet requirements-max 5 passengers and max car mass 2000')
        if name == 'car_mass' and value > 2000:
            raise IllegalCarError('car doesn\'t meet requirements-max 5 passengers and max car mass 2000')
        super().__setattr__(name, value)

    # total mass
    def total_mass(self):
        return self.car_mass + self.pax_count * 70


# custom error
class IllegalCarError(Exception):
    def __init__(self, message):
        super().__init__(message)


# example
car1 = Car(4, 1999, 8)
print('total weight:', car1.total_mass())
