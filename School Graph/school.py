import json
path = 'C:/Users/FallUpBoy/Desktop/Python projects/school graph/school.json'
with open(path, 'r') as f:
	data = json.loads(f.read())
print("What do you want to check?")
print("1.The most popular student in class")
print("2.The most popular teacher in class")
print("3.How many people are in school")
print("4.All students whoose First Name starts with 'M'")
print("5.All teachers whoose Last Name starts with 'G'")
operation = int(input("Choose the number (1, 2, 3, ...): "))
def most_frequent(friendsList):
    counter = 0
    num = friendsList[0]

    for a in friendsList:
        curr_frequency = friendsList.count(a)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = a
    return num

def most_frequent2(favTeacherList):
    counter = 0
    num = favTeacherList[0]

    for b in favTeacherList:
        curr_frequency = favTeacherList.count(b)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = b
    return num

if operation == 1:
    friendsList = []
    for i in data['students']:
        friendsList.extend(i['friends'])
    for i in data['students']:
    	if i['id'] == most_frequent(friendsList):
		    print("The most popular student in class is:", i['name'])
elif operation == 2:
    favTeacherList = []
    for i in data['students']:
        favTeacherList.append(i['favorite_teacher']) 
    for i in data['teachers']:
        if i['id'] == most_frequent(favTeacherList):
            print("The most popular teacher in class is:", i['name'])
elif operation == 3:
    studentsAmount = []
    teachersAmount = []
    for i in data['students']:
        studentsAmount.append(i['id'])
    for i in data['teachers']:
        teachersAmount.append(i['id'])
    print("There are", len(studentsAmount + teachersAmount), "people in school.")
