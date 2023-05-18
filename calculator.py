"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    input_string = input("Enter an operation to complete: ")
    tokens = input_string.split(" ")

    if 'q' in tokens:
        print("\tYou will now quit the calculator.")
        break

    if len(tokens) < 2:
        print("\tMissing a number or operation!")
        continue

    operation = tokens[0]
    num1 = tokens[1]

    if len(tokens) < 3:
        num2 = 0
    else:
        num2 = tokens[2]

    if not num1.isdigit() or not num2.isdigit():
        print("\tPlease provide numbers to run a calculation!")
        continue
    elif operation == '+':
        print(add(num1, num2))
    elif operation == '-':
        print(subtract(num1, num2))
    elif operation == '*':
        print(multiply(num1, num2))
    elif operation == '/':
        print(divide(num1, num2))
    elif operation == 'square':
        print(square(num1))
    elif operation == 'cube':
        print(cube(num1))
    elif operation == 'pow':
        print(power(num1, num2))
    elif operation == 'mod':
        print(mod(num1, num2))
    else:
        print("\tcommand not recognized")