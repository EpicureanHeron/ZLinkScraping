import pandas as pd

data = pd.read_csv('http://z.umn.edu/shortener/urls/154723/csv/click_data.csv')


print(data)

## THIS DISPLAYS THE ROWS!!! 
print(data.shape[0] -1)