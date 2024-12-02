import random

def choice():
    you=input("""s for snake
w for water
g for gun
Enter your choice: """)
    if(you=="w" or you=="s" or you=="g"):
        return you   
    else:        
        print("Enter a valid character.")
        return choice()

computer=random.choice(["s","w","g"])
you=choice()
s_w_g={"s":1,"w":-1,"g":0}
you_choice=s_w_g[you]
computer_choice=s_w_g[computer]
print(f"You chose {you} and computer chose {computer}")

if (computer_choice==you_choice):
    print("Draw")
elif(computer_choice==-1 and you_choice==1):
    print("You Win")
elif(computer_choice==-1 and you_choice==0):
    print("Computer win")
elif(computer_choice==1 and you_choice==-1):
    print("Computer win")
elif(computer_choice==1 and you_choice==0):
    print("You Win")
elif(computer_choice==0 and you_choice==-1):
    print("You Win")
elif(computer_choice==0 and you_choice==1):
    print("Computer Win") 

# Better code
# import random

# def choice():
#     you = input("""Choose:
#     s for Snake
#     w for Water
#     g for Gun
# Enter your choice: """)
#     if you in ["s", "w", "g"]:
#         return you
#     else:
#         print("Enter a valid character.")
#         return choice()

# # Computer's random choice
# computer = random.choice(["s", "w", "g"])
# you = choice()

# # Display choices
# print(f"\nYou chose {you} and the computer chose {computer}.\n")

# # Game logic
# if you == computer:
#     print("It's a Draw!")
# elif (you == "s" and computer == "w") or (you == "w" and computer == "g") or (you == "g" and computer == "s"):
#     print("You Win!")
# else:
#     print("Computer Wins!")
