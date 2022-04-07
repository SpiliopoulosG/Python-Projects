# Calculator

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def power(n1, n2):
    return n1 ** n2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "**" : power
}

starting_num = int(input("What's the first number?:\n"))
while True:
    # Logic of Calculation
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation:\n")
    next_num = int(input("What's the next number?:\n"))

    calculation_function = operations[operation_symbol]
    result = calculation_function(starting_num, next_num)

    # Prints Answer
    print(f"{starting_num} {operation_symbol} {next_num} = {result}")
    starting_num = result

    shall_stop = input("Do you wish to continue or stop?\n")
    if shall_stop.lower() == "stop":
        break


