# # open the weather_data.csv. Use .readlines() to create a list named data tha contains the values from the .csv file.
# with open("weather_data.csv") as file:
#     names = file.readlines()
#     writer.

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# mean_list = data["temp"].mean()
# print(mean_list)


# max_list = data["temp"].max()

# print(max_list)
# print(data[data.day == "Monday"])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
mon_fahrenheit = (monday_temp * 1.8) + 32
print(mon_fahrenheit)
