import os
import requests
from django.utils.timezone import now

RANDOM_CAT_IMAGE_URL = 'https://api.thecatapi.com/v1/images/search'
def random_image_url():
    return requests.get(url=RANDOM_CAT_IMAGE_URL).json()[0]['url']

def random_image_download(dir_address: str):
    image_url = random_image_url()
    image_name = image_url.split('/')[-1]

    if not os.path.exists(dir_address):
        os.makedirs(dir_address)

    with open(os.path.join(dir_address, image_name), 'wb') as image:
        image.write(requests.get(image_url).content)

    return image_name





def user_photo_location(user, file):
    today = now()
    return f'users/{user.get_full_name()}/photos/{today.year}/{today.month}/{today.day}/{file}'

#
# from django.contrib.sessions.backends.db import SessionStore
#
#
# class MySession(SessionStore):
#     def flush(self):
#         """
#         O'zgaritirilgan flush metodi.
#         Joriy sessiya ma'lumotlarini o'chirib tashlaydi va yangi kalitni yaratadi.
#         """
#         self.clear()
#
#         self.delete()
#
#         self._session_key = self.create()  # Yangi sessiya kalitini yaratadi
#
#         # Qo'shimcha amallar yoki logika qo'shishingiz mumkin
#         print("Sessiya ma'lumotlari o'chirildi va yangi kalit yaratildi:", self._session_key)
