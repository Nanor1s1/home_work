k=int(input("Введите курс: "))
p=int(input("введите процент: "))
d=int(input("введите кол-во дней: "))

for i in range(1, d+1):
    k=k*(1+p/100)
    print(f"курс в {i} день: {round (k)}")