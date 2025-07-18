with open ("12_Tables.txt","a") as file:
    num=int(input("Enter the number you want the table of:"))
    list2=[num*i for i in range(1,11)]
    file.write(str(list2) + "\n")