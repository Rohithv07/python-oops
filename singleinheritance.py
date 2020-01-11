class Apple:
    manufacture="Apple Inc."
    contactWebsite="www.apple.com"

    def contactDetails(self):
        print("To contact us log on to ",self.contactWebsite)

class MacBook(Apple):
    def __init__(self):
        self.year=2017
    def manufactureDetails(self):
        print("This MacBook was manufatured in the year {} by {}".format(self.year,self.manufacture))

macBook=MacBook()
macBook.manufactureDetails()
macBook.contactDetails()