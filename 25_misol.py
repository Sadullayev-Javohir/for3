"""n butun soni va x haqiqiy soni berilgan (n > 0, |x| < 1). Quyidagi
yig'indini hisoblovchi programma tuzilsin.
"""

n = int(input("n sonini kiriting: "))
x = int(input("x sonini kiriting: "))


    
for i in range(1, n + 1):
    s = ((-1) ** i - 1) * (x ** i) / i
print(s)
