n = int(input("Введите число n: "))

for i in range(100, n+1):
    if str(i) == str(i)[::-1]:
        print(i)