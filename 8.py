def hello():                  #function defination
    print("hello World")
hello()                       #function call

def goodDay(name):            #function with argument 
    print("Good Day, " + name)
goodDay("Ram")
goodDay("Raju")
goodDay("Rohan")

def goodDay(name,ending="Thank you"):     #function with multiple argument 
    print(f"Good Day {name}")             #uses default parameter value if no value is given at func arg
    print(ending)
goodDay("Ram","Thank you")
goodDay("Raju","Good night")
goodDay("Ramu")

def avg(a,b):
    c=(a+b)/2
    return c                   #return in function
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
average=avg(a,b)
print(average)

def fac(n):
    if(n==0 or n==1):
        return 1
    return n*(fac(n-1))
num=int(input("Enter a number:"))
print(f"The factorial of {num} is {fac(num)}")
# OR
# factorial=fac(num)
# print(f"The factorial of {num} is {factorial}")