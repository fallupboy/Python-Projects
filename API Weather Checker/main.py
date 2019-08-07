import pycountry
import requests
import geocoder
import datetime
import time

city_arr = []
humidity = []
date = []
temp = []
wind = []
desc = []

cityCheck = True
while cityCheck:
    city_name = input("Enter city name: ")
    map_key = 'YOUR_MAP_KEY'
    city_get_url = 'http://www.mapquestapi.com/geocoding/v1/address?key=' + map_key + '&location=' + city_name + '&maxResults=30'
    city_data = requests.get(city_get_url)
    city_data = city_data.json()

    city_arr = []
    for i in city_data['results'][0]['locations']:
        if i['adminArea5'] == "":
            continue
        city_arr.append(pycountry.countries.get(alpha_2=i['adminArea1']).name + ", " + i['adminArea5'] + " " + i['adminArea3'])
    if city_arr == []:
        print("City not found! Try again.")
    else:
        cityCheck = False    

for i, value in enumerate(city_arr, 1):
    print(i, value)

errorCheck = True
while errorCheck:
    try:
        choice = int(input("Choose your city (1, 2, 3...): "))
        print(city_arr[choice - 1])
        errorCheck = False
    except ValueError:
        print("Invalid input.")
    except IndexError:
        print("Invalid input.")
g = geocoder.mapquest(city_arr, method='batch', key=map_key)
lat = g.lat
lon = g.lng

app_id = 'YOUR_APP_ID'
weather_get_url = 'http://api.openweathermap.org/data/2.5/forecast?lat=' + str(lat) + '&lon=' + str(lon) + '&appid=' + app_id + '&mode=json&units=metric'
weather_data = requests.post(weather_get_url)
weather_data = weather_data.json()

for lists in weather_data['list']:
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

path = 'YOUR_PATH'
with open(path, "a+") as file:
    date = datetime.datetime.now().strftime("%m/%d/%y | %H:%M:%S")
    file.write('Logged data at: ' + str(date) + " | Location: " + city_arr[choice - 1] + '\n')
print()
print("*" * 80)
input("Press ENTER to exit")
exit(0)
