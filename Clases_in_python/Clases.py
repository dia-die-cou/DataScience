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


import time


class Car:
    # north = 1
    # east = 2
    # south = 3
    # west = 4
    def __init__(self, custom_speed, name):
        self.position = 0
        self.speed = 10
        self.name = name

    def drive(self):
        self.position += self.speed

    def print_info(self):
        print(self.name, "is current at", self.position,
              "at a speed of", self.speed)

    # def __add__(self, other):
    #     new_car


time1 = time.time()
BMW = Car(0, "BMW")

'''
for i in range(1, 10):
    BMW.speed = i
    BMW.drive()
    BMW.print_info()
'''


result = time.time() - time1
print(result)

'''
10 + 10

int(10).__add__(int(10))
'''

'''
c = Car(10)

c = object.__new__(Car)
Car.__init__(c, 10)
'''

'''
len(car)
car.__len__(car)
'''

'''
print(dir(__builtins__))
'''
