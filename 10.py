class employee:
    name= "fjan"
    salary=12434
    lang="py"

    def get_info(self): #This is a menthod. we need to use self keyword compulsory
        print(f"The language is {self.lang} and salary is {self.salary}")
    
    def greet(self): #It is also method where we also have to use self
        print("Hello Goodmorning")


harry=employee()
print(harry.name, harry.salary)


rohan=employee()
rohan.surname="Roro" #this is an instance attribute and name,salary and lang class attribute 
print(rohan.name, rohan.surname, rohan.lang)


rohan.name="Rohan" #instance attribute take preference over class attribute during assignment and retrival
print(rohan.name, rohan.surname, rohan.lang)

rohan.greet()
rohan.get_info()
employee.get_info(rohan) #It is functionally the same as rohan.ret_info(), the only difference is syntactic sugar. Even though it looks like we’re not passing any arguments in rohan.ret_info(), under the hood, It implicitly passes the instance rohan as the first argument (self) to the method.


#In the above class we used .greet() func by passing the object but it is not using any attributes of object, so we use @staticmethod instead of self to not pass the whole class.
class students:
    name="sgfa"
    salary=1637

    @staticmethod
    def greet():
        print("Goodmorning")

    def __init__(self):     #dunder method which is automatically called everytime when an object is created
        print("I am creating an object.")
    
harry=students()



class company:
    name="ghbhuj"
    location="suafgayfa"
    pincode="238762"

    def __init__(self,name,location,code):
        self.name=name
        self.location=location
        self.code=code
        print(f"The name is {self.name} and the location is {self.location} which has the pincode {self.pincode}")

mohan=company("mohan","yfyfa",782649)
