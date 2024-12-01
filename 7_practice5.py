num=int(input("Enter a number: "))
total=0
for i in range(num+1):
    total+=i
print(total)


# Faster code
num = int(input("Enter a number: "))
total = num * (num + 1) // 2  
print(total)