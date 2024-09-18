stipendia=0
stipendia1=int(input("Enter the stipedia of: "))
rashodi=0
rashodi1=int(input("Enter the rashodi of: "))
start=0
months=int(input("Enter the number of months: "))

# Calculate the amount of money after 12 months

for i in range(months):
    stipendia += stipendia1
    rashodi += rashodi1
start_sum=rashodi-stipendia

print(f"The initial amount of money: {start_sum}")
print(f"The stipendia of money: {stipendia}")
print(f"The rashodi of money: {rashodi}")

