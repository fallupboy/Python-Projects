import json
path = 'C:/Users/FallUpBoy/Desktop/Python projects/school graph/school.json'
print("What do you want to check?")
print("1.The most popular student in class")
print("2.The most popular teacher in class")
print("3.How many people are in school")
print("4.All students whoose First Name starts with 'M'")
print("5.All teachers whoose Last Name starts with 'G'")
operation = int(input("Choose the number (1, 2, 3, ...): "))

with open(path, 'r') as f:
	data = json.loads(f.read())
	if operation == 1:
		friendsList = []
		for i in data['students']:
			friendsList.extend(i['friends'])

		def most_frequent(friendsList):
			counter = 0
			num = friendsList[0]

			for a in friendsList:
				curr_frequency = friendsList.count(a)
				if(curr_frequency > counter):
					counter = curr_frequency
					num = a
			return num
		print("The most popular student is:", data['students'][(most_frequent(friendsList)) - 1]['name'])
		print("ID:", data['students'][most_frequent(friendsList) - 1]['id'])
	elif operation == 2:
		favTeacherList = []
		for i in data['students']:
			favTeacherList.extend(i['favorite_teacher'])

		def most_frequent(favTeacherList):
			counter = 0
			num = favTeacherList[0]

			for b in favTeacherList:
				curr_frequency = favTeacherList.count(b)
				if(curr_frequency > counter):
					counter = curr_frequency
					num = b
			return num
		# print("The most popular teacher is:", data['teachers'][]['name']) ***CONFUSED***