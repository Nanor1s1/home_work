from random import randint
a=[]
while len(a) <= 20:
    n = randint(1,50) 
    a.append(n)
a.sort()
sum_a=sum(a)
avg_a=sum(a)/(len(a))
print(a)
print("наибольшее значение: ",a[20]) # задание 7
print("наименьшее значение: ",a[0]) # задание 8
print("сумма :",sum_a) # задание 9
print("среднее значение: ",avg_a) # залание 10 

