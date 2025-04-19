# file=open("9_practice1.txt","r")
# data=file.read()
# print(data.__contains__("twinkle"))
# file.close()

with open("9_practice1.txt","r") as myfile:
    content=myfile.read().lower()
    if ("twinkle" in content):
        times=content.count("twinkle")
        print(f"Word twinkle is present in the file {times} times")
    else:
        print("Word twinkle is not present in the file")
