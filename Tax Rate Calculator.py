print("Choose the number of state you are living in")
print("1.New York")
print("2.Florida")
print("3.California")
print("4.Illinois")
choice = int(input("Your choice is: "))
summary = int(input("Now type your price you must pay in a shop: "))
if choice == 1:
    print("Your final price is:", summary * 0.09 + summary, "$")
elif choice == 2:
    print("Your final price is:", summary * 0.06 + summary, "$")
elif choice == 3:
    print("Your final price is:", summary * 0.07 + summary, "$")
elif choice == 4:
    print("Your final price is:", summary * 0.06 + summary, "$")
