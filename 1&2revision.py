print("hello world!")
# this is a comment line we can also use shortcut ctrl+/
'''
this is a multi line comment line
'''
print('''
      
    we can also use this to write in multiple lines
    we can also use triple" 
      ''')
a=12#This is int
b="12"#this is string
c=12.21#this is float
print(type(a))
print(type(b))
print(type(c))

#we can take input from using with the help of "input() function"
number1=input('enter number ')#but this is stored in the form of string so we need to use int() to convert into numbers
number2=int(input("enter a number "))
print(type(number1))
print(type(number2))
# print (number1)
# print (number2)

number3=int(input("enter a number "))
print("sum of number2 and number3 is",number2+number3)

print("remainder when number2 is divided by number3 is",number2%number3)

print("number2 is equal to number3",number2==number3)

print((number2+number3)/2,"is an average")

print(number3*number3,number3**2,number3**3)
