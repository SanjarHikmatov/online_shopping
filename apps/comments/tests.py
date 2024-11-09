# from django.test import TestCase

# Create your tests here.
# lst = ['1', '2', '3', '4']
# print(lst[0:-2])
um = 123
box = {}  # Bo'sh lug'atni boshlaymiz

index = 0  # Lug'atda raqamlarni saqlash uchun indeks
asd = 'abc'  # Bu satrni indeks oshirish uchun ishlatishimiz mumkin

while um > 0:
    box[index] = um % 10  # Har bir raqamni lug'atga qo'shamiz
    print(box)  # Har bir iteratsiyani chiqaramiz
    um = um // 10  # Sonning oxirgi raqamini olib tashlaymiz
    index += asd  # Indeksni oshiramiz, lekin bu yerda 'asd' uzunligi bo'yicha oshiramiz

print(box)  # Natijani chiqaramiz
 # Natijani chiqaramiz
