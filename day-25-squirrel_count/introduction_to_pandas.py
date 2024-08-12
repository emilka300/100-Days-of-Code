# reading data from weather_data.csv
import csv
import pandas

# using csv's library
weather_open = open("weather_data.csv", "r")
weather_read = csv.DictReader(weather_open)
temperatures = []
for line in weather_read:
    temperatures.append(int(line['temp']))

print(temperatures)

# using pandas' library
data = pandas.read_csv("weather_data.csv")
print(data['temp'])
print(data.temp)
data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(temp_list)
print(data['temp'].mean())
max_temp = data['temp'].max()
print(max_temp)
print(max(temp_list))

print(data[data.day == "Monday"])

print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
monday_temp_F = monday.temp*1.8+32
print(monday_temp_F)

print("")
print("--------------------------------------------------")
# create a dataframe from scratch

students_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

stud_data = pandas.DataFrame(students_dict)
print(stud_data)
stud_data.to_csv("new_data.csv")
