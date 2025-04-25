with open("9_practice6.txt") as f:
    data1=f.read()

with open("9_practice8.txt") as f:
    data2=f.read()

if data1==data2:
    print("Both file has same data.")
else:
    print("Both file has different data.")