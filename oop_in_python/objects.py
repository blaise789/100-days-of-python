class Organism:
    alive = True


class Person(Organism):
    weight = None
    height = None

    # class variable
    def __init__(self):
        pass
        # self.weight = weight
        # self.height = height

    def eat(self):
        print(self)


class Student(Person):
    def __init__(self, height):

        super().__init__()


p = Person()
# p.eat()
p.height = 3
h = p.height
print(h)
