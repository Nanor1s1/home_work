n=int(input("введите кол-во чиcел: "))
s=0
pn=1
for i in range(1, n+1):
    m=int(input("введите  чиcло: "))
    s+=m
    pn*=m
    am=s/2
    
print("сумма всех чисел :", s)
print("произведение всех чисел :", pn)
print("среднее арифметическое всех чисел :", am)