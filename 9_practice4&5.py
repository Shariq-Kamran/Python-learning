word=["donkey","monkey"]

with open ("9_practice4&5.txt","r+") as f:
    data=f.read()
    for i in word:
        data = data.replace(i, "#" * len(i))
    f.seek(0)
    f.truncate()
    f.write(data)