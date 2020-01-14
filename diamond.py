class A:
    def method(self):
        print("this method belongs to class A")


class B(A):
    def method(self):
        print("this method belonfs to class B") #everytime the method is overrriden,that method will be involed by thr derived class

    pass

class C(A):
    def method(self):
        print("this method belonfs to class C")  # if we overriden in 2 different classes,the derived class will invoke based on the order

    pass

class D(B,C):  #the order given inside parenthesis decides the output

    pass

d=D()
d.method()