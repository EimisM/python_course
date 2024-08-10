from typing import Tuple

# Define math function
def math(a: int, b: int) -> Tuple[int, int, float, float]:
    addition = a + b
    subtract = a - b
    division = a / b
    multiply = a * b
    return addition, subtract, division, multiply

# Define function to take user input
def get_user_number() -> int:
    while True:
        user_input = input("Insert a number ")
        if not user_input.isdigit():
            print("The value is not a number, please try again")   
            continue
        else:
            user_input = int(user_input)
            break
    return user_input

# Call fuction to assign user input
user_input1 = get_user_number()
user_input2 = get_user_number()

# Use function to do the math
result = math(user_input1, user_input2)
print(result)