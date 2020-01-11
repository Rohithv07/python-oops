class Employee:
    name="Ben"
    designation="Sales Executive"
    salesMadeThisWeek=6
    def hasAchieved(self):
        if(self.salesMadeThisWeek>=5):
            print("target achieved")
        else:
            print("target not achieved")
employee1=Employee()
print employee1.hasAchieved()