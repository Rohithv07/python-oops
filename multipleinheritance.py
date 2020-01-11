class OperatingSystem:
    multicasting=True
    name="Mac os"
class Apple:
    website="WWW.Apple.Com"
    name="Apple"
class MacBook(OperatingSystem,Apple):
    def __init__(self):
        if self.multicasting is True:
            print ("True and visit {}".format(self.website))
            print(self.name)#here shows the mac os as it executes based on the order given in base class
mac=MacBook()
