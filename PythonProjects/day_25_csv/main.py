# with open("weather_data.csv") as data:
#     new_data = data.readlines()
#     data = []
#     for i in range(1, len(new_data)):
#         data.append(new_data[i])
#         print(new_data)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)

# data_dict = data.to_dict()
# print(data_dict)

# data_list = data["temp"].to_list()
# print(int(sum(data_list)/len(data_list)))       # To give the average of the list

# mean = data["temp"].mean()
# print(mean)                                       # To give the average from an inbuilt function mean()

# maxi = data["temp"].max()
# print(maxi)

# mini = data["temp"].min()
# print(mini)

# Instead of using ["temp"], we can use data.temp

# mini = data.temp.min()
# print(mini)

# Check if a column/attribute contains a specific value

# data_true = data[data.day == "Monday"]
# print(data_true)

# Print when it has the maximum temperature
# maxi = data["temp"].max()
# data_true = data[data.temp == maxi]
# print(data_true)

# Print a specific value in a row
# maxi = data.temp.max()
# data_true = data[data.temp == maxi]
# print(data_true.condition)

# data_true = data[data.day == "Tuesday"]
# temp = data_true.temp[1]
# temp = temp*1.8 + 32
# print(temp)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# Initialise a DataFrame from scratch                      # DataFrame is 2D, Series is 1D. Refer to documentation
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_weather.csv")
# Create a csv using in-built library in pandas

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231208.csv")
# color = data["Primary Fur Color"]
# print(color)
# print(len(color))
# color_gray = data[color == "Gray"]
# print(len(color_gray))
# color_cinnamon = data[color == "Cinnamon"]
# print(len(color_cinnamon))
# color_black = data[color == "Black"]
# print(len(color_black))

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231208.csv")
# color = data["Primary Fur Color"].to_list()
# gray = 0
# cinnamon = 0
# black = 0
# for yes in color:
#     if yes == "Gray":
#         gray += 1
#     elif yes == "Cinnamon":
#         cinnamon += 1
#     elif yes == "Black":
#         black += 1
# print(gray)
# print(cinnamon)
# print(black)


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231208.csv")
color_gray = len(data[data["Primary Fur Color"] == "Gray"])
color_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
color_black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [color_gray, color_cinnamon, color_black]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("Squirrel_color_count.csv")
print(new_data)




