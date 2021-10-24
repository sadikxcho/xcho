#1.1 dan 70 gacha sonlar orasidan 8 ga qoldiqsiz bo'linadigan sonlarni chiqaring.
for n in range(1,71):
    if n%8==0:
        print(n)

#2.10 dan 30 gacha sonlarni yigindisi hisoblang.
yigindi = 0
for n in range(10,31):
    yigindi=yigindi+n
print(yigindi)    

#3.1 dan 100 gacha faqat juft sonlarning yig'indisini hisoblang.
yigindi = 0
for n in range(1,101):
    yigindi=yigindi+2
print(yigindi)

#4 ga bolganda qoldiq 3 ga teng bolgan sonlarni chiqarish dasturini tuzing. 1 dan 100 gacha oraliqda.
for n in range(1,101):
    if n/4==3:
        print(n)

#5.* ikki ta a va b sonlari berilgan, shulardan kattasini aniqlash dasturini tuzing.

a = 14
b = 156
print(a<b)

#6.** 3 ta sondan kattasini aniqlash dasturini tuzing. masalan: a=4, b=8, c=2  natija: bu sonlardan eng kattasi 8 . 

son = int(input("sonni kiriting: "))
son2 = int(input("sonni kiriting: "))
son3 = int(input("sonni kiriting: "))
print(f"bu sonlardan eng kattasi {son2}")
          
#import math kutib honadan foydalanilgan misol

import math

daraja = math.pow(15,2)
print(daraja)
