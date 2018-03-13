from abc import ABCMeta, abstractmethod
class Vehicle(object):

    """Created parent class with attributes that
    will be inherited by child classes"""

    __metaclass__ = ABCMeta

    base_sales_price = 0
    wheels = 0

    def __init__(self, miles, make, model, year, sold_on):
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sales_price(self):
        """ Return the sale price for this vehicle float amount"""
        if self.sold_on is not None:
            return 0.0 # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """ Return the price for which we would pay to purchase the vehicle"""
        if self.sold_on is None:
            return 0.0 # Not sold yet
        return self.base_sales_price - (.10 * self.miles)

    @abstractmethod
    def vehicle_type(self):
        """ Return a string representing the type of vehicle this is. """
        pass

class Car(Vehicle):

    base_sales_price = 8000
    wheels = 4

    def vehicle_type(self):
        """ Return string representing the type of vehicle this is """
        return 'car'

class Truck(Vehicle):

    base_sales_price = 10000
    wheels = 4

    def vehicle_type(self):
        """ Return string representing the type of vehicle """
        return 'truck'

class Motorcycle(Vehicle):

    base_sales_price = 4000
    wheels = 2

    def vehicle_type(self):
        """ Return a string representing the type of vehicle """
        return 'motorcycle'


