class Car:
    def __init__(self, pax_count, car_mass, gear_count):
        self.pax_count = pax_count
        self.car_mass = car_mass
        self.gear_count = gear_count

        if self.pax_count < 1 or self.pax_count > 5 or self.car_mass > 2000:
            raise IllegalCarError('car doesn\'t meet requirements')

    def total_mass(self):
        return self.car_mass + self.pax_count * 70


class IllegalCarError(Exception):
    def __init__(self, message):
        super().__init__(message)


car1 = Car(4, 1999, 8)
car1.pax_count = 3
if car1.pax_count < 1 or car1.pax_count > 5:
    raise IllegalCarError('car doesn\'t meet requirements')