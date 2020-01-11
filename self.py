#class Employee:
  #  def employeeDetails():
   #     pass

#employee =Employee()
#employee.employeeDetails()#this is treated as Employee.employeeDetails(employee).so shows an error and this can be rewritten using giving some argument given below

class Employee:
    def employeeDetails(self):
        self.name='rohith'   #lifespan of self is higher and can be used in another method also  
        print(self.name )
        age='30'
        print(age)
    def printEmployeeDetails(self):
        print("Name:",self.name)
     #   print("Age",age)  -this will show error
employee=Employee()
employee.employeeDetails()
employee.printEmployeeDetails()