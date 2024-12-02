def greater_of(x,y,z):
    if(x>y and x>z):
        print(f"{x} is the greatest number.")
    elif(y>x and y>z):
        print(f"{y} is greatest number.")
    else:
        print(f"{z} is the greatest number.")

num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
num3=int(input("Enter a number: "))
greater_of(num1,num2,num3)