# three ways to write a string 
a="sda"
b='sda'
c="""sda""" # or '''sda'''

word = "amazing" 
word[1: 6: 2] # "mzn"
word [:7] # word [0:7] – 'amazing' 
word [0:] # word [0:7] – 'amazing'

print(len(word))
print(word.endswith("ing"))

count = word.count("g")
print(count)

capital= word.capitalize()
print(capital)

replaced_string=word.replace("a","z")
print(replaced_string)

name=input("enter your name: ")
print(f"Good afternoon {name}")

string="sjand a dnak  sadawd" #string is immutable
print(string.find("  "))
str2=string.replace("  "," ")
print(str2)

list1=[1,23.3,32,"words","s"] #list is mutable
print(list1[1])

l1 = [1,8,7,2,21,15]
print(l1)
l1.sort()
print(l1)
'''
l1.sort(): updates the list to [1,2,7,8,15,21]
l1.reverse(): updates the list to [15,21,2,7,8,1]
l1.append(8): adds 8 at the end of the list
l1.insert(3,234) #This will add 234 at 3 index
l1.pop(2): Will delete element at index 2 and return its value.
l1.remove(21): Will remove 21 from the list.
'''

tuple1=() #It is same as list but with only one difference that it is immutable
tuple2=(1,) 

fruits=[]
i=int(input("Enter the number of Fruits:"))
for n in range(i):
    fruits.append(input("Enter fruit name:"))
print(fruits)

marks=[]
for i in range(6):
    marks.append(int(input("Enter student marks:")))
marks.sort()
print(marks)

a = (7, 0, 8, 0, 0, 9)
print(a.count(0))