numbers=[]
for i in range(4):
    temp=int(input("Enter a number you want to store:"))
    numbers.append(temp)
print(numbers)
if(numbers[0]>numbers[1] and numbers[0]>numbers[2] and numbers[0]>numbers[3]):
    print(numbers[0],"is the greatest number.")
elif(numbers[1]>numbers[0] and numbers[1]>numbers[2] and numbers[1]>numbers[3]):
    print(numbers[1],"is the greatest number.")
elif(numbers[2]>numbers[1] and numbers[2]>numbers[0] and numbers[2]>numbers[3]):
    print(numbers[2],"is the greatest number.")
else:
    print(numbers[3],"is the greatest number.")

