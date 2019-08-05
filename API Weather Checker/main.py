import requests
import datetime
import time

humidity = []
date = []
temp = []
wind = []
desc = []

errorCheck = True
while errorCheck:
    try:
        city_name = input("Enter city name: ")
        app_id = '7b9d5008d599ec2605884c73a1a4bcb2'
        complete_url = 'http://api.openweathermap.org/data/2.5/forecast?q=' + city_name + '&appid=' + app_id + '&mode=json&units=metric'
        data = requests.post(complete_url)
        data = data.json()

        for lists in data['list']:
            date.append(lists['dt_txt'])
            humidity.append(lists['main']['humidity'])
            temp.append(lists['main']['temp'])
            wind.append(lists['wind']['speed'])
            desc.append(lists['weather'][0]['description'])

        print("*" * 80)
        print("\t\t" + "Details about the forecast of the city " + city_name + " for 5 days:\n")
        print('{:^25}{:^20}{:^20}{:^20}{:^20}'.format("Date", "Description", "Temperature", "Wind", "Humidity\n"))
        for i in range(len(humidity)):
            print('{:^25}{:^20}{:^20}{:^20}{:^20}'.format(str(date[i]), desc[i], str(round(temp[i], 1)) + " C\N{DEGREE SIGN}", str(int(wind[i])) + " m/s", str(humidity[i]) + " %"))
        errorCheck = False
    except KeyError:
            print("City not found. Try again.")
            print()


path = 'C:/Users/FallUpBoy/Desktop/Python projects/API Weather Checker/log.txt'
with open(path, "a+") as file:
    date = datetime.datetime.now().strftime("%m/%d/%y | %H:%M:%S")
    file.write('Logged data at: ' + str(date) + '\n')
print()
print("*" * 80)
input("Press ENTER to exit")
exit(0)
