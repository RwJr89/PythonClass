theSum = 0.0
theAverage = 0.0
count = 0
data = input("Enter a number: ")
while data != "":
    count = count+1
    number = float(data)
    theSum += number
    data = input("Enter the next number: ")
theAverage = theSum / count
print("The sum is", theSum)
print("The average is", theAverage)
