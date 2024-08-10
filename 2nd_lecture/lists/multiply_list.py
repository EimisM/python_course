# Define list of values
my_list = [1, 2, 3, 4, 5]

# Define multiply_list
def multiply_list(my_list):
    result = 1
# Define loop to iterate every number in the list
    for number in my_list:
        result *= number
    return result

# Print the outcome
print(multiply_list(my_list))