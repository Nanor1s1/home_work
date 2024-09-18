stipendia1=0
stipendia2=0
rashodi1=rashodi2=0
start=0
months=int(input("Enter the number of months: "))

for i in range(1,months,2):
    stipendia1 += 100
    rashodi1+=120
    rashodi1*=1.03

for i in range(0,months,2):
    stipendia2  += 100
    rashodi2+=120
    rashodi2*=1.05

stipendia=stipendia1+stipendia2
rashodi=rashodi2+rashodi1
# Print the result
print(f"The stipendia of money: {stipendia}")
print(f"The rashodi of money: {round(rashodi,2)}")
print(f"The initial amount of money: {round(rashodi-stipendia,2)}")
