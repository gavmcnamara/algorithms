class Vehicle(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    @staticmethod
    def make_car_sound():
        print 'VRooooom!'

car = Vehicle('Ford', 'Mustang')

print car.wheels

print car.make

print Vehicle.wheels

print Vehicle.make_car_sound()
