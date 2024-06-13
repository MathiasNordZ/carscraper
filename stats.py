import pandas as pd
import numpy as np

df = pd.read_csv('carinfo.csv')

df['Pris'] = df['Pris'].str.replace('\\s+', '', regex=True)
df['Kilometer'] = df['Kilometer'].str.replace('\\s+', '', regex=True)

df['Pris'] = pd.to_numeric(df['Pris'], errors='coerce')

cleaned_price = []
for value in df['Pris']:
    try:
        cleaned_price.append(int(value))
    except ValueError:
        cleaned_price.append(np.nan)

df['Pris'] = cleaned_price

x1 = 0
y1 = 550000

x2 = 0
y2 = 150000

x3 = 2010
y3 = 2020

price_range = (x1, y1)
mileage_range = (x2, y2)

year_data = df[(df['Årsmodell'] >= x3) & (df['Årsmodell'] <= y3)].copy()
year_data.loc[:, 'Kilometer'] = pd.to_numeric(year_data['Kilometer'], errors='coerce')

price_filtered_data = year_data[
    (year_data['Pris'] >= price_range[0]) &
    (year_data['Pris'] <= price_range[1])
]

mileage_price_filtered_data = price_filtered_data[
    (price_filtered_data['Kilometer'] >= mileage_range[0]) &
    (price_filtered_data['Kilometer'] <= mileage_range[1])
]

average_price = mileage_price_filtered_data['Pris'].mean()
median_price = mileage_price_filtered_data['Pris'].median()
max_price = mileage_price_filtered_data['Pris'].max()
min_price = mileage_price_filtered_data['Pris'].min()


