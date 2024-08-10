# Define a class Calculator with 
class Calculator:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b
    # Define calculations
    def add(self) -> int:
        return self.a + self.b
    def divide(self) -> float:
        return self.a / self.b
    def multiply(self) -> int:
        return self.a * self.b
    def subtract(self) -> int:
        return self.a - self.b

# Gather user input and validate that user is inserting an actual int
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

# Assign user inbut to a and b attributes in Calculator object
a = get_user_number()
b = get_user_number()

# Assign calculator to the a and b attributes
result = Calculator(a,b)

# Create a line based user interface to figure what calculation user want to perform
choice = 1
if choice != 0:
    print("0. Exit")
    print("1. Add")
    print("2. Divide")
    print("3. Multiply")
    print("4. Subtract")
    choice = int(input("Enter a choice: "))
    if choice == 1:
        print(" Result: ", result.add())
    elif choice == 2:
        print(" Result: ", result.divide())
    elif choice == 3:
        print(" Result: ", result.multiply())
    elif choice == 4:
        print(" Result: ", result.subtract())       