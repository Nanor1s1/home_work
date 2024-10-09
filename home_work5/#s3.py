from random import randint
a=[]
while len(a) <= 20:
    n = randint(1,50) 
    a.append(n)
a.sort()
print(a)
print(a[19])