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

def most_frequent(friendList):
	counter = 0
	num = friendList[0]

	for a in friendList:
		curr_frequency = friendList.count(a)
		if(curr_frequency > counter):
			counter = curr_frequency
			num = a
	return num

def get_student_id(idList):
	num2 = idList[0]

	for b in idList:
    	if b = most_frequent(friendList):
    		num2 = b
	return num2
		
friendList = []    	
for i in data['students']:
	friendList.extend(i['friends'])

idList = []
for i in data['students']:
	idList.extend(i['id'])

if operation == 1:
	print(get_student_id(idList))