# Tip Calculator
print('Welcome to the tip calculator!')

# Inputs
bill = float(input("What was the total bill? \n"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? \n"))
people = int(input("How many people to split the bill? \n"))

# Calculations
total_bill = bill + (tip / 100) * bill
person_bill = round(total_bill / people, 3)

# Prints the total amount a person should Pay
print(f"Each person should pay ${person_bill}")
