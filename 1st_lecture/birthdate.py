name = input("What's your name? ")
age = input("What's your age? ")

from datetime import date

# Get current year

current_date = date.today()

# Access the year attribute of the current year
current_year = current_date.year

# Calculate birthdate
birthdate = (current_year - int(age))

print(f"Hello, your name is {name} and you were born on {birthdate}")