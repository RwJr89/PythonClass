# Modify the following code

# Request the input
mass = float(input("Enter the object's mass:")) 
velocity = float(input("Enter the object's velocity:"))  

# Compute the results
momentum = mass * velocity
ke = 1/2 * mass * velocity ** 2

# Display the results
print("The object's momentum is",momentum,"kilograms", \
      "The object's kinetic energy is",ke,"kilograms")
