price = int(input("Введите  цену товара: "))
discount = int(input("Введите увеличение процента скидки после каждой покупки: "))
start_money = int(input("введите начальное количество денег: "))

total_discount = 0
total_price = 0
for i in range(0,100,discount):
    total_discount += (1-(discount / 100))
    total_price += price * total_discount
    
    if total_price >=start_money:
        break


print(f"Сумма, которую вы потратите: {total_price:.2f}")
print(f"Остаток денег: {start_money-total_price:.2f}")
print(total_discount)
