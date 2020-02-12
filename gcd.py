smaller = int(input("Enter the smaller number:"))
larger = int(input("Enter the larger number:"))
for i in range(1, smaller+1):
    if smaller % i == 0 and larger % i == 0:
        gcd = i

print("The greatest common divisoris",gcd)
