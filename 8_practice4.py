def sum_of(n):
    if n==1:
        return 1
    return n+(sum_of(n-1))

num=int(input("Write a number:"))
print(f"{sum_of(num)}")
