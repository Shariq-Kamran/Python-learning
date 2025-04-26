class Employee:
    def __init__(self):
        self._salary=0
        self.increment_value=0
    
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,value):
        if value<0:
            print("Invalid Amount entered.")
        else:
            self._salary=value

    def increment(self,percentage):
        self.increment_value=self.salary+self.salary*(percentage/100)
        return self.increment_value

e=Employee()
e.salary=500
print(e.increment(100))