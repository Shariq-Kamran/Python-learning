names=["Rohan","Raj","Ramu"]
new_name=input("Enter your name: ")
if (new_name in names):
    print("This name already exist.")
else:
    names.append(new_name)
print(names)
