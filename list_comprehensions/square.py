def is_square(n):
    return int(n**0.5) ** 2 == n

user_input = int(input("Please insert a number "))
print(is_square(user_input))