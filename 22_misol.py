"""n butun soni va x haqiqiy soni berilgan (n > 0). Quyidagi yig'indini hisoblovchi programma
tuzilsin. (Olingan natija taxminan e**x ga yaqinlashadi.)"""

n = int(input("n sonini kiriting: "))
x = int(input("x sonini kiriting: "))
factorial = 1

if (n > 0):
    for i in range(1, n + 1):
        factorial *= i
        s = 1 + x ** i / factorial
    print(s)
else:
    print(f"{n} > 0 ? {n} katta bo'lishi kerak 0 dan")
    