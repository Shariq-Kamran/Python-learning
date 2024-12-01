# My version
# num=int(input("Enter a number: "))

# for i in range(2,num):
#     if(num%i==0):
#         print("Number is not prime.")
#         break
# else:
#     print("Number is prime.")
        
# Correct code
num = int(input("Enter a number: "))
if num <= 1:
    print("Number is not prime.")
else:
    for i in range(2, int(num ** 0.5) + 1):  # Check divisors up to √num
        if num % i == 0:
            print("Number is not prime.")
            break
    else:
        print("Number is prime.")