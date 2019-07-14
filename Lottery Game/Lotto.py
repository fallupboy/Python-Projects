from random import random
import datetime
path = 'C:/Users/FallUpBoy/Desktop/Python projects/Lottery Game/log.txt'
now = datetime.datetime.now()

loop = True
attemps = 4
jackpot = 25000
rating = "rating"
back = "return"

print(20 * "-", "Welcome to Python Lotto! Today's jackpot is 25000$", 20 * "-")
print(23 * "-", "You will have 5 attemps to win our jackpot", 23 * "-")
print(25 * "-", "Every unlucky attemp will lower jackpot", 25 * "-")
print()
nameCheck = True
while nameCheck:
        name = input("Please type your name to play or type 'rating' to see last 10 games history: ")
        if name == "":
            print("That is not an option")
        else:
            nameCheck = False

if name == rating:
    ct = 1
    try:
        for line in reversed(open(path).readlines()):
            if(ct <=10): 
                print(ct, line.rstrip())
            else: 
                break
            ct+=1
        input("Press ENTER to exit: ")
    except:
        print("Error occured. Please try again later.")
    exit(0)

while loop:
    winNum = random() * 10 + 1
    winNum = int(winNum)    
    
    intCheck = True
    while intCheck:  
        try:
            userNum = int(input("Enter a number to play (1 - 20): "))
            intCheck = False
        except ValueError:
            print("That is not an option")
            userNum = None

    if attemps == 0:
        print("You are out of attemps. The winning number was", winNum, "| You won 0 $")
        with open(path, 'a') as log:
            log.write('Name -- {0} ::: Prize -- 0 $$$ ::: Date -- {1}\n'.format(name, now.strftime("%d/%m/%Y %H:%M:%S")))
        input("Press ENTER to exit: ")
        exit(0)

    if int(userNum) < 1 or int(userNum) > 20:
        print("Invalid number. Choose between 1-20")
        exit(0)

    if int(userNum) == winNum:
        print("Congratulations! You won", jackpot, "$")
        with open(path, 'a') as log:
            log.write('Name -- {0} ::: Prize -- {1} $$$ ::: Date -- {2}\n'.format(name, jackpot, now.strftime("%d/%m/%Y %H:%M:%S")))
        input("Press ENTER to exit: ")
        exit(0)

    else:
        print("Unlucky attemp... The winning number was", winNum, "| Try again!")
        print("Attemps remained:", attemps, "| Jackpot is lowered to", jackpot / 2, "$")
        print(50 * "-")
        attemps -= 1
        jackpot /= 2
