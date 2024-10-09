b=input("Enter: ")
a= list(b)
print(a)
for i in a:
    if i =='a' or i == 'e' or i == 'o':
        a.remove(i)
res_a = ''.join(a)
print(res_a)
