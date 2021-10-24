savol = ("yaxshi korgan kitobingini kiriting: ")
savol += "(toxtatish uchun 'stop' deb yozing): "
natija = ' '
while natija != 'stop':
    natija = input(savol)
    if natija != 'stop':
        print(input(natija))
print("toxtatildi!")

son = 10
while son>=0:
    print(son)
    son=son-1

yigindi = 0
n = 1
while n<=10:
    yigindi+=n
    n+=1
print(f"""1 dan 10 gacha sonlar yigindisi {yigindi}""")


son = 0 
while son<60:
    son += 1
    if son%1!=0:
       continue
    else:
        print(son)

i = 1
while i <=60:
    print(i)
    i += 1
