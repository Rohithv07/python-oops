import abc,six
from abc import ABCMeta,abstractmethod

@six.add_metaclass(abc.ABCMeta)
class Shape():
    @abc.abstractmethod
    def area(self):
        return 0      #abstract cant have any object


class Square:
    side=4
    def area(self):
        print(self.side**2)

class Rect:
    width=5
    length=10
    def area(self):
        print(self.width * self.length)

square=Square()
rect=Rect()
square.area()
rect.area()