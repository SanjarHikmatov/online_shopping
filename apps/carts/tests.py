# from django.test import TestCase
num = 634
numbox = ''

while num > 0:

        n = num % 10
        n1 = numbox + str(n)

        num = num // 10
        continue
    print(numbox)

print(num % 10)