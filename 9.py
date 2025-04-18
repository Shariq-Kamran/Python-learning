data=open("9_1.txt")
text=data.read()
print(text)
data.close()

st="lhsdasdaddas"
f=open("9_1.txt","w")
f.write(st)
f.close()

d=open("9_2.txt","w")
text2=d.write("sdaagg")
d.close()

file=open("9_3.txt")
# text3=file.readline()
# print(text3, type(text3))

# text4=file.readline()
# print(text4,type(text4))

# text5=file.readline()
# print(text5,type(text5))
# file.close()

text3=file.readline()
while(text3!=""):
    print(text3)
    text3=file.readline()
file.close()


with open("9_3.txt") as words:
    print(words.read())         #No need for closing the file if we use with statement