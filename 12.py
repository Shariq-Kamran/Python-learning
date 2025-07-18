#Walrus Operator 
print(happy:=True)


if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")


foods=list()
while food:=input("What food do you like:") != "quit":
    foods.append(food)


# TYPES DEFINITIONS
a:int=21

name:str="Harry"

def sum(a:int,b:int) -> int:
    return a+b
#This method is helpfull for programmers to understand the datatypes of the variables while programming/coding easily


# You can import List, Tuple and Dict types from the typing module like this:
from typing import List,Tuple,Dict,Union

# List of integers 
numbers: List[int] = [1, 2, 3, 4, 5] 

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85} 

# Union type for variables that can hold multiple types 
identifier: Union[int, str] = "ID123" 
identifier = 12345 # Also valid



#match case in python is similar to switch statement found in C language
def web_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case _:                     #this is defult case
            return "Unknown status"
    
print(web_status(404))
print(web_status(400))



# DICTIONARY MERGE & UPDATE OPERATORS
dict1={"first":1,"second":2}
dict2={"fourth":4,"third":3}
merged=dict1|dict2
print(merged)




#Exception Handling in Python 
try:
    num=int(input("Enter a number:"))

except ValueError as v:
    print(v)
    print("Enter a valid number.")

except Exception as e:
    print(e)



#Raising exceptions
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))

if (b==0):
    raise ZeroDivisionError("You cant divide number with zero")
else:
    print(f"Division of a nd b is {a/b}")
#next code



#try with else
try:
    a=0
    # b==0

except Exception as e:
    print(e)

else:
    print("Else is only run if the try runs successfully without any errors/exceptions.")


#try with  finally
finally:
    print("this code runs even if the try block fails or runs successfully.this runs even the above code have return in function")



#IF __NAME__== ‘__MAIN__’
if __name__=="__main__":
    #this code will be only executed if the present file is executing this code and not the imported file
    print("We are directly running this code")
    print(__name__)



#enumerate
l=[3,54,2452,5634,134]
for index,item in enumerate(l):
    print(f"the item in index {index} is {item}")



#list Comprehensions
# List Comprehension is an elegant way to create lists based on existing lists.
list1=[1,2,3,4,5,6]
# list2=[]
# for item in list1:
#     list2.append(item*item)
# print(list2)

#this can be done much easier using list comprehension
list2=[i*i for i in list1]
print(list2)