'''
class car:

    position = 0
    speed = 10

    def move:
        car.position += car.speed
        print("car is at {}",.format(car.position))

nicos_car = car
bobs_car = car

nicos_car.move()
nicos_car.move()
nicos_car.move()

bobs_car.move()
bobs_car.move()

# result is 50
'''

'''
class car:

    position = 0
    speed = 10

    def move:
        car.position += car.speed
        print("car is at {}",.format(car.position))


car.move()
car.move()
car.move()

# result is 30
'''

'''
class car:
    def create_new_car():    
        position = 0
        speed = 10
        return position, speed

    def move(position, speed):
        position += speed
        print("car is at {}".format(position))
        return position, speed

nicos_car = car
nicos_info = nicos_car.create_new_car()


nicos_info = nicos_car.move(*nicos_info)
nicos_info = nicos_car.move(*nicos_info)
nicos_info = nicos_car.move(*nicos_info)

print(nicos_info)
print(*nicos_info)
print(nicos_info[0], nicos_info)

'''

'''
class car:
    def create_new_car(position, speed):
        car_info = {
        "position": 0,
        "speed": 10
        }
        return car_info

    def move(car_info):
        car_info["position"] += car_info["speed"]
        print("car is at {}".format(position))

nicos_car = car
nicos_info = nicos_car.create_new_car()

nicos_info.nicos_car.move(car_info)
nicos_info.nicos_car.move(car_info)
nicos_info.nicos_car.move(car_info)
'''

class Car:
    def __init__(self, name, speed):
        self.name = name
        self.position = 0
        self.speed = speed

    def move(self):
        self.position += self.speed
        print(self.name + " is now at position " + str(self.position))

nicos_car = Car("Nico", 10)

nicos_car.move()
nicos_car.move()
nicos_car.move()


bobs_car = Car("Bob", 15)

bobs_car.move()
bobs_car.move()
bobs_car.move()