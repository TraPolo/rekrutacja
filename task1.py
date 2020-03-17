class Car:

    def __init__(self, pax_count, car_mass, gear_count):
        self.pax_count = pax_count
        self.car_mass = car_mass
        self.gear_count = gear_count

        # checking requirements
        if self.pax_count < 1 or self.pax_count > 5 or self.car_mass > 2000:
            raise IllegalCarError('car doesn\'t meet requirements')

    # total mass
    def total_mass(self):
        print('total weight', self.car_mass + self.pax_count * 70)


# custom error
class IllegalCarError(Exception):
    def __init__(self, message):
        super().__init__(message)

#example
car1 = Car(4, 1999, 8)
car1.total_mass()
