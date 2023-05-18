"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

operations = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide,
  'square': square,
  'cube': cube,
  'power': power,
  'mod': mod
}

# Replace this with your code
while True:
    input_string = input("Enter an operation to complete: ")
    tokens = input_string.split(" ")

    # exit program
    if 'q' in tokens:
        print("\tYou will now quit the calculator.")
        break

    # input validation for missing operator/operand
    if len(tokens) < 2:
        print("\tMissing a number or operation!")
        continue

    operation = tokens[0]
    num1 = tokens[1]

    if len(tokens) < 3:
        num2 = "0"
    else:
        num2 = tokens[2]

    if not num1.isdigit() or not num2.isdigit():
        print("\tPlease provide numbers to run a calculation!")
        continue

    if operation in operations:
        calculation_function = operations[operation]
        answer = calculation_function(float(num1), float(num2))
        print(answer)
    else:
        print("\tcommand not recognized")