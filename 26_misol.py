"""n butun soni va x haqiqiy soni berilgan. Quyidagi yig'indini hisoblovchi
programma tuzilsin."""

n = int(input("n sonini kiriting: "))
x = int(input("x sonini kiriting: "))

for i in range(1, n + 1):
    
    s = (-1**i) * (x**(2 * n+1)) / (2 * i + 1)

print(s)