"""n butun soni berilgan (n > 0). Bir sikldan foydalangan holda 
quyidagi yig'indini hisoblovchi programma tuzilsin. (Olingan natija
taxminan e = exp(1) ga yaqinlashadi)"""

n = int(input("n sonini kiriting: "))
factorial = 1

if (n > 0):
    for x in range(1, n + 1):
        factorial *= x
        s = 1 + 1 / factorial
    print(s)
else:
    print(f"{n} > 0 ? {n} katta bo'lishi kerak 0 dan")