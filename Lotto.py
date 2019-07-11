from random import random

loop = True
attemps = 4
jackpot = 1000

print(20 * "-", "Welcome to Python Lotto! Today's jackpot is 1000$", 20 * "-")
print(23 * "-", "You will have 5 attemps to win our jackpot", 23 * "-") 
print(20 * "-", "Every unlucky attemp will raise jackpot by twice", 20 * "-")

while loop:
    winNum = random() * 20 + 1
    winNum = int(winNum)
    userNum = int(input("Enter a number to play (1 - 20): "))
    if userNum < 1 or userNum > 20:
        print("Invalid number. Choose between 1-20")
        exit(0)
    if userNum == winNum:
        print("Congratulations! You won", jackpot, "$")
        input("Press ENTER to exit")
        exit(0)
    else:
        print("Unlucky attemp... The winning number was", winNum, ".", "Try again!") 
        print(attemps, "attemps remained. Jackpot is raised to", jackpot * 2, "$")
        print(50 * "-")
        attemps -= 1
        jackpot *= 2
    if attemps < 0:
        print("Sorry, but there are no attemps left."), 
        input("Press ENTER to exit")
        exit(0)
