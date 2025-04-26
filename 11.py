class employee:   #Base class
    company="GE"

    def show(self):
        print(f"The name is {self.name} and salary is {self.salary}.")
    
    def __init__(self,name, salary):
        self.name=name
        self.salary=salary

class programmer(employee):   #Derived class
    company="infotech"
    lang="python"

    def showlan(self):
        print(f"The language is {self.lang}")    
#By inheritance we can use method and attributes of base class in derived class
#and we can also overwrite or add new attributes or methods in derived class

a=employee("harry",312123)
b=programmer("mohan",87589)

a.show()
b.showlan()
b.show()


# Types of inheritance
# 1.Single inheritance
# 2.Multiple inheritance : Here child inherits from multiple parents classes.
# 3.Multilevel inheritance : Here child class becomes a parent for another child class.



# super() method is used to access the method of a super class in the derive class.
class student:
    def __init__(self):
        print("constructor of student.")

class class9(student):
    def __init__(self):
        print("Constructor of class9.")

class class10(class9):
    def __init__(self):
        super().__init__()
        print("Constructor of class10.")

a=class10()




# CLASS METHOD
# A class method is a method which is bounf to the class and not the object of the class.
# @classmethod decorator is used to create a class method.

class class1:
    a=4

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

o=class1()
o.a=989    #This value can't be used in a class method.As it is an instance attribute.
o.show()





class for_property:

    @property
    def name(self):
        return (f"The name is {self.fname} {self.lname}")
    
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

nm=for_property()
nm.name="Harry Khan"
print(nm.name)





class Temperature:
    def __init__(self,celsius):
        self._celsius=celsius

    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self,value):
        if value < -273.15:
            print("Temperature below absolute zero!")
            return
        else:
            self._celsius = value
            
    @property
    def fahrenheit(self):
        return (self._celsius*9/5)+32
            
        
fe=Temperature(-66)
print(f"Temperature in Fahrenheit: {fe.fahrenheit}°F")

# for i in range(4):
#     fe.celsius=int(input("Enter the Temperature in Celsius: "))
#     print(f"The temperature in Fahrenheit is {fe.fahrenheit}")


