sentence=input("Write your comment: ").lower()
if (("buy now"in sentence) or ("free"in sentence) or ("click this"in sentence)):
    print("scam")
else:
    print("not scam")
