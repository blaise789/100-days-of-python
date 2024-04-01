class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def __int__(self):
        pass

    def drive(self):
        print("This " + self.model + " is driving")


car1 = Car()
car1.model = "benz"
print(car1.model)
