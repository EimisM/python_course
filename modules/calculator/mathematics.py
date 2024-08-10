from modules.calculator.math_mod import math

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

user_input1 = get_user_number()
user_input2 = get_user_number()

result = math(user_input1, user_input2)
print(result)