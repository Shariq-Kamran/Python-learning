"""We are going to write a program that generates a random number and asks the user to guess it.
If the player's guess is higher than the actual number, the program displays “Lower number please”. Similarly, if the user's guess is too low, the program prints “higher number please” When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.
Hint: Use the random module"""

# import random

# def guess_num(randnum,attempts):
#     attempts=attempts+1
#     guess=int(input("Guess the number: "))
#     if randnum==guess:
#         print("You guessed the correct number.")
#         return attempts
#     elif randnum>guess:
#         print("Higher number please.")
#         return guess_num(randnum,attempts)
#     elif randnum<guess:
#         print("Lower number please.")
#         return guess_num(randnum,attempts)

# randnum=random.randint(1,100) 
# attempts_no=0
# print(guess_num(randnum,attempts_no))


import random
randnum=random.randint(1,100) 
attempts_no=0
guess=-1
while randnum!=guess:
    attempts_no+=1  
    guess=int(input("Guess the number: "))
    if randnum>guess:
        print("Higher number please.")
    elif randnum<guess:
        print("Lower number please.")

print(f"You have guessed the correct number in {attempts_no} attempts.")