x1 = int(input("Введите координату x1: "))
y1 = int(input("Введите координату y1: "))
x2 = int(input("Введите координату x2: "))
y2= int(input("Введите координату y2: "))

if not 1 <= x1 <= 8 or not 1 <= y1 <= 8 or not 1 <= x2 <= 8 or not 1 <= y2 <= 8:
    print("Ошибка!")
elif abs(x2 - x1) == 1 and abs(y2 - y1) == 2:
    print("YES")
elif abs(x2 - x1) == 2 and abs(y2 - y1) == 1:
    print("YES")
else:
    print("NO")
