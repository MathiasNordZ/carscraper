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

x1 = int(input('Nedre prisgrense: '))
y1 = int(input('Øvre prisgrense: '))

x2 = int(input('Nedre kilometergrense: '))
y2 = int(input('Øvre kilometergrense: '))

x3 = int(input('Årsmodell fra: '))
y3 = int(input('Årsmodell til: '))

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

output = f'''
Info om årsmodell fra {x3} til {y3}, i pris-intervallet {x1} kr til {y1} kr og kilometerstand mellom {x2} km og {y2} km.
Gjennomsnittlig pris er {average_price:.0f} kr.
Medianpris er {median_price:.0f} kr.
Høyeste pris er {max_price:.0f} kr.
Laveste pris er {min_price:.0f} kr.
'''

print(output)


