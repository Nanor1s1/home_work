k = int(input("Введите число K: "))
n = int(input("Введите число N: "))
s=0
for i in range (k,n+1):
    if i%2==0:
        s+=i
print("сумма четных чисел от", k, "до", n, "равна", s)