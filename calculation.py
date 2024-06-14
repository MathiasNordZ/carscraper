import pandas as pd
import numpy as np

def value_calculation(price_range = (0, 550000), mileage_range = (0, 150000), year_range = (2010, 2020)):
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

    year_data = df[(df['Årsmodell'] >= year_range[0]) & (df['Årsmodell'] <= year_range[1])].copy()
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
    
    return {
        'average_price': average_price,
        'median_price': median_price,
        'max_price': max_price,
        'min_price': min_price
    }

