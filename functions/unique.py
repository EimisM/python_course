# Define a new function
def unique_strings(lst: list) -> list:
    def has_unique_chars(s):
        return len(s) == len(set(s))
    
    # Iterate over each string in the list and filter those with unique characters
    return [s for s in lst if has_unique_chars(s)]

# Define list
lst = ["hello", "world", "abc", "deff", "unique", "apple", "dog"]

# Call the function and store result in a variable
result = unique_strings(lst)

# Print the result
print(result)