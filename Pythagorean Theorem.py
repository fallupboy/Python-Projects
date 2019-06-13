import math
print("1.The first catheter")
print("2.The second catheter")
print("3.Hypotenuse")
toDo = int(input("Choose a number what you want to find: "))
if toDo == 1:
    secondCatheter = int(input("Set the value to the second catheter: "))
    hypotenuse = int(input("Set the value of the hypotenuse: "))
    print("The first catheter equales", math.sqrt(hypotenuse ** 2 - secondCatheter ** 2))
elif toDo == 2:
    firstCatheter = int(input("Set the value to the first catheret: "))
    hypotenuse = int(input("Set the value of the hypotenuse: "))
    print("The second catheter equales", math.sqrt(hypotenuse ** 2 - firstCatheter ** 2))
elif toDo == 3:
    firstCatheter = int(input("Set the value to the first catheret: "))
    secondCatheter = int(input("Set the value to the second catheter: "))
    print("Hypotenuse equales", math.sqrt(firstCatheter ** 2 + secondCatheter ** 2))
else:
    print("Incorrect value! Try again")
    exit(0)
input("Press 'ENTER' to exit")
