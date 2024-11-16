Person={
    "name":"kamran","age":14,"USN":677
} #this is an dictionary
print(Person.items())
print(Person.values())
Person.update({"age":19,"marks":0})
print(Person)
print(Person["age"])

new_person={}#this is an empty dict
print(type(new_person))

set1={1,235,41,7}#this is a set,it can only have values and no keys
print(type(set1))
set_e=set()#this method is used to create empty set
set_e.add("name")
print(set_e)
# we can use union and intersection on sets
#set are not hashable