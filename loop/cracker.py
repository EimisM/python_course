import random
pin = int(input("Please insert 4 digit pin code for your safe "))

while True:
    cracker = random.randint(0000,9999)
    if cracker != pin:

        print(f"pin {cracker} is incorrect")
    else:
        print(f"The pin is {cracker}, you have successfully cracked the code")
        break