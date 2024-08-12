import pandas as pd
data = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

squirrel_data = pd.read_csv(data)
color_count = squirrel_data.groupby("Primary Fur Color")[["Primary Fur Color"]].count()
color_count.rename(columns={"Primary Fur Color": "Count"}, inplace=True)
color_count.rename(index={"Cinnamon": "Red"}, inplace=True)
print(color_count)

color_count.to_csv("squirrel_count.csv")
