a = int(input("введите первое чило! "))
b = int(input("введите вттрое чило! "))

if a==b:
    print("числа равны")
else:
    print("числа не равны")

if b==0:
    print("на 0 нельзя делить")
else:
    c = a%b
    if c == 0:
        print("число картно")
    else:
        print("не кратно")
