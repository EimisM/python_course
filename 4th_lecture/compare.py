number1 = int(input("Insert first number "))
number2 = int(input("Insert second number "))

if number1 > number2:
    print(f"{number1} is bigger than {number2}")
elif number1 == number2:
    print(f"{number1} is equal to {number2}")
else:
    print(f"{number1} is smaller than {number2}")