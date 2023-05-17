"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    input_string = input("Enter an operation to complete: ")
    token = input_string.split(" ")

    operation = token[0]
    num1 = int(token[1])
    num2 = int(token[2])

    if 'q' in token:
        print("You will now quit the calculator.")
        break
    else:
        if operation == '+':
            print(add(num1, num2))
        if operation == '-':
            print(subtract(num1, num2))
        if operation == '*':
            print(multiply(num1, num2))
        if operation == '/':
            print(divide(num1, num2))
        if operation == 'square':
            print(square(num1))
        if operation == 'cube':
            print(cube(num1))
        if operation == 'pow':
            print(power(num1, num2))
        if operation == 'mod':
            print(mod(num1, num2))