height = float(input("Enter the height:"))
bouncy_index = float(input("Enter the bounciness index:"))
bounces = int(input("Enter the number of bounces:"))

distance = 0

while bounces > 0:
    distance = distance + height
    height = height * bouncy_index
    distance = distance + height
    bounces -= 1
print("The distance traveled is:", distance)



