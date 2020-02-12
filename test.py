# Edit the code below (from Project 4)
import math
base = float(input("Enter the base: "))
height = float(input("Enter the height: "))
area = base * height
print("The area is", area, "square units.")

# Calculate area of a cube

edge = float(input("Enter cube's edge:"))
area = 6 * (edge * edge)
print("The surface area is", area, "square units")

# Write a program that takes the radius of a sphere
# (a floating-point number) as input and then outputs
# the sphere’s:

# Diameter(2 × radius)
# Circumference(diameter × π)
# Surface area(4 × π × radius × radius)
# Volume(4/3 × π × radius × radius × radius)

radius = float(input("Enter the radius:"))
diameter = 2 * radius
circumference = diameter * math.pi
surfaceArea = 4 * math.pi * radius * radius
volume = 4/3 * math.pi * radius * radius * radius

# Printed results

print("Diameter:", diameter)
print("Circumference:", circumference)
print("Surface area:", surfaceArea)
print("Volume", volume)

# An object’s momentum is its mass multiplied by
# its velocity.

# Write a program that accepts an object’s mass(in kilograms)
# and velocity(in meters per second) as inputs,
# and then outputs its momentum.

mass = float(input("Enter the objects mass:"))
velocity = float(input("Enter objects velocity:"))
momentum = mass * velocity
print("The objects's momentum is", momentum, "kilograms")

# Modify the following code

# The kinetic energy of a moving object is given by
# the formula KE = ½mv2
# where m is the object’s mass and v is its velocity.

# Modify the program you created in Project 5 so that
# it prints the object’s kinetic energy as well as
# its momentum.

# Request the input
mass = float(input("Enter the object's mass: "))
velocity = float(input("Enter the object's velocity: "))

# Compute the results
momentum = mass * velocity
ke = 1/2 * (mass * velocity ** 2)

# Display the results
print("The object's momentum is", momentum)
print("The object's kinetic energy is:", ke)