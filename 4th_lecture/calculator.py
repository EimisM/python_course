number1 = int(input("Please insert first number "))
number2 = int(input("Please insert second number "))
operator = input("Please insert an operator for the equation (+, -, * or /) ")

if operator == '+':
    result = number1 + number2
    print(f"{number1} {operator} {number2} = {result}")
elif operator == '-':
    result = number1 - number2
    print(f"{number1} {operator} {number2} = {result}")
elif operator == '*':
    result = number1 * number2
    print(f"{number1} {operator} {number2} = {result}")
elif operator == '/':
    result = number1 / number2
    print(f"{number1} {operator} {number2} = {result}")
elif operator != '+' or '-' or '*' or '/':
    print("Operator is incorrect, please read the instructions carefully")