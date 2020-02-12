iterations = int(input("Enter the number of iterations:"))

pi_div = 0
current_iteration = 1
for i in range(1, iterations+1):
    if(i % 2 != 0):
        pi_div = pi_div + 1 / current_iteration
    else:
        pi_div = pi_div - 1 / current_iteration

    current_iteration = current_iteration + 2
    pi_value = pi_div * 4
print("The approximation of pi is", pi_value)