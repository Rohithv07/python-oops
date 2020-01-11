#Public == membername
#protected == _membername
#private == __membername

class Car:
    numberofwheels=4
    _color='black'
    __year=1098 #name mangling-_Car __year

class Bmw(Car):
    def __init__(self):
        print(self._color)

car=Car()
print car.numberofwheels
print car._Car__year
bmw=Bmw()

