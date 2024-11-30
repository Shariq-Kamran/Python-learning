i=1
while(i<6):
    print(i)
    i+=1

list=[1,"string",223,"2313",534.3]
i=0
while(i<len(list)):
    print(list[i])
    i+=1

for i in range(4):
    print(i)

for i in list:
    print(i)

# A for loop is used to iterate through a sequence like list, tuple, or string [iterables]

# range(start, stop, step_size) # step_size is usually not used with range()

l= [1,7,8] 
for item in l:
    print(item) 
else: 
    print("done") # this is printed when the loop exhausts!

for i in range (0,80):
    if i==3:
        continue  #It will skip the iteration
    if i==7:    
        break     #It will break the loop
    print(i)

for item in l:
    pass # without pass, the program will throw an error.It could be used while the development of the program.