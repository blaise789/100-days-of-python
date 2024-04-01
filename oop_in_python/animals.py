class Prey:
    def __init__(self):
        pass

    def flees(self):
        print("the  prey flees from the predators")


class Predator:

    def hunts(self):
        print("the animal hunts others for food")


class Fish(Predator, Prey):
    pass


fish = Fish()
fish.flees()
