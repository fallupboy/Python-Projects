stateTaxes = {'New York': 0.09, 'Florida': 0.06, 'California': 0.07, 'Illinois': 0.06}
print("Choose the state you are living in")
print("1.New York")
print("2.Florida")
print("3.California")
print("4.Illinois")
choice = input("Your choice is (type the name of state): ")
summary = int(input("Now type your price you must pay in a shop: "))
if choice in stateTaxes:
    print("Your price is:", stateTaxes[choice] * summary + summary)
else:
    print("The state was not found. Check if the state was written correctly and try again")
