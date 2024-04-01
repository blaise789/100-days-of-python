# method chaining
class Car:
    def turn_on(self):
        print("you start the engine")
        return self

    def drive(self):
        print("you drive the car")
        print(self)
        return self

    def brake(self):
        print("you step on the brakes")
        return self

    def turn_off(self):
        print("you stop the engine")
        return self


car = Car()
car.drive(). \
    brake(). \
    turn_off()
