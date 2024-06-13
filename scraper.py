from bs4 import BeautifulSoup
import requests
import time
import csv

base_url = 'https://www.finn.no/car/used/search.html?model=1.749.7967&page='
pages = 6

price = []
make = []
year = []
mileage = []

for page in range(1, pages + 1):
    url = f'{base_url}{page}'
    
    r = requests.get(url)
    
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html5lib')
        
        make_elements = soup.find_all(class_='sf-search-ad-link link link--dark hover:no-underline')
        info_elements = soup.find_all(class_ = 'mb-8 flex justify-between whitespace-nowrap font-bold')

        for element in make_elements:
            link_text = (element.get_text(strip=True))
            make.append(link_text)
        
        for info in info_elements:
            span_element = info.find_all('span')

            if len(span_element) > 0:
                year_span = (span_element[0].get_text(strip=True))
                year.append(year_span)
            else:
                year.append('')
                
            if len(span_element) > 1:
                mileage_span = (span_element[1].get_text(strip=True))
                mileage.append(mileage_span)
            else:
                year.append('')
                
            if len(span_element) > 2:
                price_span = (span_element[2].get_text(strip=True))
                price.append(price_span)
            else:
                year.append('')
        
        time.sleep(1)
    else:
        print('Failed to retrieve page')

price_unit = 'kr'
mileage_unit = 'km'

price = [sub.replace(price_unit,'').strip() for sub in price]
mileage = [sub.replace(mileage_unit,'').strip() for sub in mileage]
        
with open('carinfo.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    writer.writerow(['Navn', 'Årsmodell', 'Kilometer', 'Pris'])
    
    for i in range(max(len(make), len(year), len(mileage), len(price))):
        row = [
            make[i] if i < len(make) else '',
            year[i] if i < len(year) else '',
            mileage[i] if i < len(mileage) else '',
            price[i] if i < len(price) else '',
        ]
            
        writer.writerow(row)