num=int(input("Enter the number you want the Multiplication table of: "))

for i in range(1,11):
    print(f"{num}x{i}={num*i}")
    i+=i

print("************************************************************************")

n=1
while(n<11):
    print(num,"x",n,"=",num*n)
    n+=1


num=int(input("Enter the number you want the reverse Multiplication table of: "))
for i in range(1,11):
    print(f"{num}x{11-i}={num*(11-i)}")
    i+=i