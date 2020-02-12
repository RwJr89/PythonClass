# Programmer: Rawle Williams
# Date: 2/11/2020
# File name: money_counting_game_williams.py

# Pseudocode:
# Coin counting

# Value of coin

PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

# Coin input request

pennies = int(input("Enter number of pennies:"))
nickles = int(input("Enter number of nickles:"))
dimes = int(input("Enter number of dimes:"))
quarters = int(input("Enter number of quarters:"))

# Coin calculation
total = PENNY_VALUE * pennies + NICKEL_VALUE * nickles + \
    DIME_VALUE * dimes + QUARTER_VALUE * quarters

# negative number input
if pennies < 0 or nickles < 0 or dimes < 0 or quarters < 0:
    print("The number should be a positive integer!")

# total  more than 100
elif total > 100:
    print("Sorry, the amount you entered was more than one dollar.")

# total less than 100
elif total < 100:
    print("Sorry, the amount you entered was less than one dollar.")

# total equals to 100
elif total == 100:
    print("The amount you entered was exactly one dollar! You win the game!")
