'''
class Car:
    # north = 1
    # east = 2
    # south = 3
    # west = 4

    position = 0
    speed = 10

    def drive():
        Car.position += Car.speed
    
    def print_info():
        print("Car is current at", Car.position)

Car.print_info()
Car.drive()
Car.drive()
Car.drive()
Car.print_info()
'''


class Car:
    # north = 1
    # east = 2
    # south = 3
    # west = 4
    def __init__(self):
        self.position = 0
        self.speed = 10

    def drive(self):
        self.position += self.speed
    
    def print_info(self):
        print("Car is current at", self.position)


BMW = Car()

BMW.print_info()
BMW.drive()
BMW.drive()
BMW.drive()
BMW.print_info()