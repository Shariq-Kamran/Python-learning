word="python"

with open("9_practice6.txt") as f:
    data = f.read()
    if word in data:
       print(f"The log contains {word}")
    else:
        print(f"The log doesn't contain {word}")
