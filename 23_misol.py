"""n butun soni va x haqiqiy soni berilgan (n > 0). Quyidagi yig'indini hisoblovchi
programma tuzilsin. (Olingan natija taxminan sin(x) ga yaqinlashadi.)"""

n = int(input("n sonini kiriting: "))
x = int(input("x sonini kiriting: "))

factorial = 1

for i in range(1, n+1):
    factorial *= 2 * i + 1
    s = ((-1) ** i) * (x ** (2 * i + 1)) / (factorial)
print(s)

