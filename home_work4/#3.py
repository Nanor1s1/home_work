n=int(input("введите кол-во чиcел: "))
c1=0
c2=0
for i in range(1, n+1):
    m=int(input("введите  чиcло: "))

    if m % 2 == 0:c2+=1
    else:c1+=1

print("кол-во четных",c2)
print("кол-во нечетных",c1)