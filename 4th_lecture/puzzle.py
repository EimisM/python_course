import random
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

number = random.choice(list)

while True:
    user_guess = int(input("Insert a number between 1 and 10 - "))
    if user_guess != number:
        print("You guessed the number incorrectly, try again ")
    else:
        break
print(f"Congratulations you've guessed the number! The number is {number}")
