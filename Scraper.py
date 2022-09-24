import requests
from bs4 import BeautifulSoup
import pandas as pd
url = input("Введіть посилання з сайту: ")
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

data = []

name = soup.find('div', class_='seller_info_name bold').text
model = soup.find('div', class_='technical-info ticket-checked').find('span', class_='argument d-link__name').text
location = soup.find('li', class_='item').find('div', class_='item_inner').text
engine = soup.find('div', class_='technical-info ticket-checked').findAll('dd', class_='')[2].text
price = soup.find('div', class_='price_value').find('strong', class_="").text
space = soup.find("div", class_="box-panel description-car").find('div', class_='technical-info').find('dd', class_='').text
kpp = soup.find("div", class_="box-panel description-car").find('div', class_='technical-info').findAll('dd', class_='')[3].text
header = ["Імя продавця", "Модель автомобіля", "Місто", "Ціна", "Мотор", "Кількість місць", "Коробка передач"]
data.append([name, model, location, price, engine, space, kpp])

df = pd.DataFrame(data, columns=header)
df.to_csv('D:\Autoria.csv', sep=';', encoding='utf-8-sig')
print(name, model, location, price, engine, space, kpp)
