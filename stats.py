import pandas as pd
import numpy as np

df = pd.read_csv('carinfo.csv')

df['Pris'] = df['Pris'].str.replace('\\s+', '', regex=True)
df['Kilometer'] = df['Kilometer'].str.replace('\\s+', '', regex=True)

cleaned_price = []
for value in df['Pris']:
    try:
        cleaned_price.append(int(value))
    except ValueError:
        cleaned_price.append(np.nan)

df['Pris'] = cleaned_price

year = int(input('Årsmodell: '))
price_range = (0, 90000)
mileage_range = (0, 200000)

year_data = df[df['Årsmodell'] == year]
year_data['Kilometer'] = pd.to_numeric(year_data['Kilometer'], errors='coerce')

price_filtered_data = year_data[
    (year_data['Pris'] >= price_range[0]) &
    (year_data['Pris'] <= price_range[1])
]

mileage_price_filtered_data = [
    (price_filtered_data['Kilometer'] >= mileage_range[0]) &
    (price_filtered_data['Kilometer'] <= mileage_range[1])
]

print(type(mileage_price_filtered_data))


