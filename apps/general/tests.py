import requests
from datetime import date

currency='EUR'
GET_CURRENCY_URL = f'https://cbu.uz/oz/arkhiv-kursov-valyut/json/{currency}/{date}/'

today = date.today()

response = requests.get(
    url=GET_CURRENCY_URL.format(date=today)
)

currency_list = ['USD', 'RUB']

for curr in currency_list:
    print(requests.get(url=GET_CURRENCY_URL.format(currency=curr,date=today)).json())
