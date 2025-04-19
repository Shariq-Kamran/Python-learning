import random

def game():
    score=random.randint(1,62)
    print(f"You are playing a game.\nYour Score={score}")
    return score

game_score=game()
with open("9_practice2.txt","r+") as data:
    hiscore=data.read()
    if hiscore=="":
        hiscore=0
    else:
        hiscore=int(hiscore)
    if game_score>hiscore:
        data.seek(0)
        data.truncate()
        data.write(str(game_score))
        print(f"You got an high score of {game_score}")
    else:
        print(f"You got an score of {game_score} and the high score is {hiscore}")
print("Game Over.")