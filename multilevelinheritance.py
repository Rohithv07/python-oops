class Animal:
    name="tiger"

class Species(Animal):
    family="cat"

class Place(Species):
    def __init__(self):
        if self.name is "tiger" and self.family is "cat":
            print("multilevel inhertance example is confirmed using {} and {}".format(self.name,self.family))

place=Place()

