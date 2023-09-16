import pandas

datafile = pandas.read_csv("weather_data.csv")
data_dict = datafile.to_dict()
print(data_dict["temp"])

data_list = datafile["temp"].to_list()
print(data_list)

print(f"Avg: {round(sum(data_list)/ len(data_dict))}")

print(datafile["temp"].max())

print(datafile.columns.to_list())

print(datafile.condition)

print(datafile[datafile.day == "Monday"])

print(f"Max temp {datafile[datafile.temp == max(datafile.temp)]}")

print(datafile.temp.mean())

print(datafile.temp.median())
