n=int(input("Enter the number: "))

for i in range(2, n+1,2):
    if n%i == 0 and i%2==0:
        print(i)
else:print("нет четных делителей")
    