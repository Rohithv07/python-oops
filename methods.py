class Employee:
    def employeeDetails(self):
        self.name="Rohith"
    @staticmethod  #used to ignore the absence of self parameter in the method
    def welcomeMessage():
        print("welcome to static method")

employee=Employee()
employee.employeeDetails()
print(employee.name)
employee.welcomeMessage()