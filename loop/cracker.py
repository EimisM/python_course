import random
pin = int(input("Please insert 4 digit pin code for your safe "))

combinations = list(range(0, 10000))

for comb in combinations:
    if comb != pin:
        print(f"pin {comb:04} is incorrect")
    else:
        print(f"The pin is {comb:04}, you have successfully cracked the code")
        break