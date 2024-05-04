import pandas as pd

# Problem 02: Read a CSV file and display the first 5 rows
data = pd.read_csv('../data/data_02.csv')
print(data.head())