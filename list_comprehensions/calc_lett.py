text = 'In this lecture we will review some additional functionalities of python built-in data structures'
string = text.replace(" " and "-", "")
my_dict = {}

for char in string:
    if char not in my_dict:
        my_dict[char] = 1
    else:
        my_dict[char] += 1

print(my_dict)