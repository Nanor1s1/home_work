stipendia1=0
stipendia2=0
stipendiab=int(input("Enter the number of: "))
rashodi1=rashodi2=0
rashodib=int(input("Enter the number of: "))
start=0
months=int(input("Enter the number of months: "))

for i in range(1,months,2):
    stipendia1 += stipendiab
    rashodi1+=rashodib
    rashodi1*=1.03

for i in range(0,months,2):
    stipendia2  += stipendiab
    rashodi2+=rashodib
    rashodi2*=1.05

stipendia=stipendia1+stipendia2
rashodi=rashodi2+rashodi1
# Print the result
print(f"The stipendia of money: {stipendia}")
print(f"The rashodi of money: {round(rashodi,2)}")
print(f"The initial amount of money: {round(rashodi-stipendia,2)}")

