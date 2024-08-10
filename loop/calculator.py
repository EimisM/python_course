# Define user input
user_input = input("Insert a sequence of numbers for the calculation - (example 1, 2, 3, 4, 5) - ")

# Convert string into list of substrings
num = user_input.split(",")
# Create a list
list_of_num = []
# Convert each substring into integer
for n in num:
    list_of_num.append(int(n))
    
avg = sum(list_of_num) / len(list_of_num)

# Do the sum calculation
print(sum(list_of_num))
print(avg)