class Employee:
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours=40
    def showNumberOfWorkingHours(self):
        print(self.numberOfWorkingHours)

class Trainee(Employee):
     def setNumberOfWorkingHours(self):
          self.numberOfWorkingHours=45 
     def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkingHours() #give the control back to the base class

employee=Employee()
employee.setNumberOfWorkingHours()
print("Number of working hours:")
employee.showNumberOfWorkingHours()
trainee=Trainee()
trainee.setNumberOfWorkingHours()
print(trainee.showNumberOfWorkingHours())
trainee.resetNumberOfWorkingHours()
print(trainee.showNumberOfWorkingHours())
