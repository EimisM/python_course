name = input("Insert your name ")
lastname = input("Insert your lastname ")
age = int(input("Insert your age "))

if age <= 21:
    print(f"Client {name} {lastname} is not allowed to go into our casino")
else:
    print(f"Client {name} {lastname} is {age} years old and is allowed to go into our casino")