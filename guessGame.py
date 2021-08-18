from os import write
import random

print("NOTE : you have only 10 chances")

randnum = random.randint(1,100)
print(randnum)

count = 10
userInput = None

while(userInput != randnum) :

    print(f"\n---> COUNT NO. : {10-count+1}")
    userInput = int(input("enter a number : "))

    if(userInput == randnum):
        print("\n #-------- You Won --------# \n")
        print(f"YOU GUESSED THE NUMBER IN {10-count+1} chance")
        break
    elif(userInput in range(randnum,randnum+10)):
        print("you are too close , and a litle bit high")
    elif(userInput in range(randnum-10,randnum)):
        print("you are too close , and a litle bit LOW")
    elif(userInput > randnum):
        print("Guess is too high")
    elif(userInput < randnum):
        print("Guess is too LOW")
    
    count-=1

    if(count == 0):
        print("\nGAME OVER :(")
        break

    print(f" ----> you have {count} turns left")

total_count = 10-count+1

with open("highscoreGame.txt") as f:
    highscore = int(f.read())

if(total_count < highscore):
    print("Your broke your prev. HighScore .... yeahhhhhhhh...")
    with open("highscoreGame.txt","w") as f:
        f.write(str(total_count))

# 1-2-3-4-5-6-7-8-9-10 
# 1 is the HIGHSCORE
# 10 is the lowestScore