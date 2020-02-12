sal = float(input("Enter the starting salary:"))
percent = float(input("Enter the annual % increase:"))
year = int(input("Enter the number of years:"))
print("\nYear Salary")
for i in range(year):
    print(i+1, sal)
    print("%.2f" % sal)
    sal = sal * (1+percent/100)
