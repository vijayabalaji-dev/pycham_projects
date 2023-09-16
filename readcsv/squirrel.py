import pandas

dataframe = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(dataframe.columns.to_list())

#unique colours in file

unique = dataframe["Primary Fur Color"].unique().tolist()
unique_colours = unique[1:]
print(unique_colours)

unique_list = []
for color in unique_colours:
    count = dataframe[dataframe['Primary Fur Color'] == color]
    unique_list.append({"colour":color, "total":len(count)})

print(pandas.DataFrame(unique_list))