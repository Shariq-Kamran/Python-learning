english_marks=int(input("Enter English marks out of 100:"))
science_marks=int(input("Enter Science marks out of 100:"))
maths_marks=int(input("Enter Maths marks out of 100:"))
total_percentage=((english_marks+science_marks+maths_marks)/300)*100
if(total_percentage<40 or english_marks<33 or science_marks<33 or maths_marks<33):
    print("You have failed")
else:
    print("You have passed")
print(total_percentage)