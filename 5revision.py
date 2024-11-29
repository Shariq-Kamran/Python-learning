dict={"key":"value","name":"shariq","language":"python","marks":100,list:[2,32,43,1,42,34]}
         # This is a dictionary ,It is Mutable
dict1={} #We can also create it like this, this is a empty dictionary

dict.update({"percent":99,"marks":89})

print(dict["name"])
print(dict["marks"])

print(dict.items())
print(dict)

print(dict.keys())
print(dict.values())

print(dict.get("marks")) #Returns NULL if not available in dictionary,which is better then dict[marks]


set1={1,"home",41,"7"} #this is a set,it can only have values and no keys
set2=set() #This is the correct way to create an empty set
#sets cannot have repeated values and it stores values in unordered way 
# sets are unindexed  
set1.add(44)
print(len(set1))
set1.remove(41)
print(set1)

num1={2,4,6,43,12,6}
num2={1,7,5,3,12,64}
print(num1.union(num2)) #OR num3=num1.union(num2)  # print(type(num3))
#We can use Union and Intersection like operations on sets
#We cant have lists in a set


#Practice

translator={"hindi_words":"english_word","ye":"this","vo":"that","hindi":"english"}
word=input("Type the word you want the translation of ")
print("the translation of",word,"is",translator.get(word))

input_numbers=set()
temp=int(input("enter the number you want to store:"))
input_numbers.add(temp)
print(input_numbers)# for loop

fav={}
name=input("enter your name:")
lang=input("enter your favorite language:")
fav.update({name:lang})
print(fav) #for loop