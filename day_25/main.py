import pandas
import matplotlib.pyplot


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data.columns = data.columns.str.replace(' ', '_')
fur_counts = data.Primary_Fur_Color.value_counts()
fur_counts.to_csv("squirel_count.csv")
