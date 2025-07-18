def list_table():
    num=int(input("enter the number you want the table of:"))
    list2=[num*i for i in list]
    return list2

list=[1,2,3,4,5,6,7,8,9,10]
print(list_table())

# easier method
# list2=[num*i for i in range(1,11)]
