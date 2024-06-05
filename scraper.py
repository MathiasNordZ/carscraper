from bs4 import BeautifulSoup
import requests
import time
import csv

base_url = 'https://www.finn.no/car/used/search.html?model=1.749.7967&page='
pages = 5

price = []
make = []
year = []
mileage = []

for page in range(1, pages+1):
    url = f'{base_url}{pages}'
    
    r = requests.get(url)
    
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html5lib')
        
        make_element = soup.find_all(class_='sf-search-ad-link link link--dark hover:no-underline')
        info_element = soup.find_all(class_ = 'mb-8 flex justify-between whitespace-nowrap font-bold')
        
        for info in info_element:
            span_element = info.find_all('span')
            if len(span_element) > 0:
                first_span = span_element[0]
                year_span = (first_span.get_text(strip=True))
                year.append(year_span)
                
            if len(span_element) > 1:
                second_span = span_element[1]
                mileage_span = (second_span.get_text(strip=True))
                mileage.append(mileage_span)
                
            if len(span_element) > 2:
                third_span = span_element[2]
                price_span = (third_span.get_text(strip=True))
                price.append(price_span)
                
        for make1 in make_element:
            make_element = info.find_all('span')
            if len(make_element) > 0:
                first_span = make_element[0]
                make_span = (first_span.get_text(strip=True))
                make.append(make_span)
        
        time.sleep(1)
    else:
        print('Failed to retrieve page')
        
with open('carinfo.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    writer.writerow(['Navn', 'Årsmodell', 'Kilometer', 'Pris'])
    
    for i in range(max(len(make), len(year), len(mileage), len(price))):
        row = []
        
        if i < len(make):
            row.append(make[i])
        else:
            row.append('')
            
        if i < len(year):
            row.append(year[i])
        else:
            row.append('')
            
        if i < len(mileage):
            row.append(mileage[i])
        else:
            row.append('')
            
        if i < len(price):
            row.append(price[i])
        else:
            row.append('')
            
        writer.writerow(row)

print(make)