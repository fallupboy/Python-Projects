import json
path = 'C:/Users/FallUpBoy/Desktop/Python projects/school graph project/school.json'
with open(path, 'r') as f:
	data = json.loads(f.read())
print("What do you want to check?")
print("1. The most popular student in class")
print("2. The most popular teacher in class")
print("3. How many people are in school")
print("4. All students whoose First Name starts with 'M'")
print("5. All teachers whoose Last Name starts with 'G'")
print("6. Favorite student among all teachers")
operation = int(input("Choose the number (1, 2, 3, ...): "))
def getFavPerson(personList):
    counter = 0
    num = personList[0]

    for a in personList:
        curr_frequency = personList.count(a)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = a
    return num

if operation == 1:
    friendsList = []
    for i in data['students']:
        friendsList.extend(i['friends'])
    for i in data['students']:
    	if i['id'] == getFavPerson(friendsList):
		    print("The most popular student in class is:", i['name'])
    input("Press 'ENTER' to exit")
elif operation == 2:
    favTeacherList = []
    for i in data['students']:
        favTeacherList.append(i['favorite_teacher']) 
    for i in data['teachers']:
        if i['id'] == getFavPerson(favTeacherList):
            print("The most popular teacher in class is:", i['name'])
    input("Press 'ENTER' to exit")
elif operation == 3:
    studentsAmount = []
    teachersAmount = []
    for i in data['students']:
        studentsAmount.append(i['id'])
    for i in data['teachers']:
        teachersAmount.append(i['id'])
    print("There are", len(studentsAmount + teachersAmount), "people in school.")
    input("Press 'ENTER' to exit")
elif operation == 4:
    studentsName = []
    letterCheckM = []
    for i in data['students']:
        studentsName.append(i['name'])
    for i in studentsName:
        if i[0] == "M":
            letterCheckM.append(i)
    if len(letterCheckM) > 0:
        print("Here are all students whoose First Name starts with 'M':")
        for i in letterCheckM:
            print(i)
    else:
        print("There are no students whoose First Name starts with 'M'")
    input("Press 'ENTER' to exit")  
elif operation == 5:
    teachersSplit = []
    letterCheckG = []
    for i in data['teachers']:
        teachersSplit.append(i['name'].split())
    for i in teachersSplit:
        if i[1][0] == "G":
            letterCheckG.append(i)
    if len(letterCheckG) > 0:
        print("Here are all teachers whoose Second Name starts with 'G':")
        for i in letterCheckG:    
            print(i[0], i[1])
    else:
        print("There are no teachers whoose Last Name starts with 'G'")
    input("Press 'ENTER' to exit")
elif operation == 6:
    favStudentList = []
    for i in data['teachers']:
        favStudentList.append(i['favorite_student'])
    for i in data['students']:
        if i['id'] == getFavPerson(favStudentList):
            print("The favorite student among teachers is:", i['name'])
    input("Press 'ENTER' to exit")
else:
    print("Invalid input")
    input("Press 'ENTER' to exit")
