from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass


class Car(Vehicle):
    color = "Green"

    # pass
    def go(self):
        print("you drive the car")


class MotorCycle(Vehicle):
    color = "Green"

    # pass
    def go(self):
        print("you ride the motorcycle")


def change_color(car_cl,cl):
    car_cl.color=cl


# vehicle = Vehicle()
car = Car()
car.go()
color = car.color
print(color)
change_color(car,"Blue")
print(car.color)

