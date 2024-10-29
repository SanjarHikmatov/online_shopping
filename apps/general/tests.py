# import requests
# from datetime import date
#
# currency='EUR'
# GET_CURRENCY_URL = f'https://cbu.uz/oz/arkhiv-kursov-valyut/json/{currency}/{date}/'
#
# today = date.today()
#
# response = requests.get(
#     url=GET_CURRENCY_URL.format(date=today)
# )
#
# currency_list = ['USD', 'RUB']
#
# for curr in currency_list:
#     res = requests.get(url=GET_CURRENCY_URL.format(currency=curr,date=today)).json()
#     print(res['Rate'])

from django.contrib.sessions.backends.db import SessionStore

class MySession(SessionStore):
    def key_salt(self):
        return "django.contrib.sessions." + self.__class__.__qualname__

# Sessiya obyekti yaratamiz
session = MySession()

# Sessiya uchun kalitni olish
session_key = session.get_session_key()
if not session_key:
    session_key = session.create()  # Yangi sessiya kalitini yaratamiz

# Saltni olish
salt = session.key_salt()

# Yakuniy kalitni yaratish
final_key = salt + session_key
print(final_key)
