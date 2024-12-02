def star_pattern(n):
    if (n==0):
        return 
    print("*"*n)
    star_pattern(n-1)

star=int(input("Enter the number of lines of stars:"))
star_pattern(star)