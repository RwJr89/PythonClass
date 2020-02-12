hourlyWage = float(input("Enter the wage:"))
regularHours = float(input("Enter the regular hours:"))
overTime = float(input("Enter the overtime hours:"))
weeklyPay = hourlyWage * regularHours
overTimeWage = hourlyWage * 1.5
overTimePay = overTime * overTimeWage
totalWage = weeklyPay + overTimePay
print("The total weekly pay is $"+str(totalWage))
