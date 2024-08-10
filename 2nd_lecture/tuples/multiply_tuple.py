# Define list of values
my_tuple = (1, 2, 3, 4, 5)

# Define multiply_tuple
def multiply_tuple(my_tuple):
    result = 1
# Define loop to reiterate every number in the list
    for number in my_tuple:
        result *= number
    return result

# Print the outcome
print(multiply_tuple(my_tuple))