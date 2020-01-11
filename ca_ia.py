class Employee:
    numberOfWorkingHours=40
    
employeeOne=Employee()
employeeTwo=Employee()
print employeeOne.numberOfWorkingHours
print employeeTwo.numberOfWorkingHours

Employee.numberOfWorkingHours=45   #class attribute
print employeeOne.numberOfWorkingHours
print employeeTwo.numberOfWorkingHours

employeeOne.name="john"  #instance attribute
print employeeOne.name

employeeOne.numberOfWorkingHours=40 #instance attribute
print employeeOne.numberOfWorkingHours