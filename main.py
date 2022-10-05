import random

spisok=[]

plus = 0
minus = 0
i = 0

while i < 15:
    i = i + 1
    z = random.randint(-100, 100)
    if z == 0:
        while z == 0:
            z = random.randint(-100, 100)
    if z > 0:
        plus = plus + z
    else:
        minus = minus + z
    spisok.append(z)
print("15 случайных чисел:", spisok)
print("Сумма положительных:", plus)
print("Сумма отрицательных:", minus)


