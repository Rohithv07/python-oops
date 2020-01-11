class Employee:

    def __init__(self,name):
        self.name=name
    
    
       
    
    def showDetails(self):
        print(self.name)

employee=Employee("pqr")  #as soon as object is created init method is invoked automatically
employee2=Employee("ppp")

employee.showDetails()
employee2.showDetails()

