text = 'In this lecture we will review some additional functionalities of python built-in data structures'
string = text.split(" ")

result = [1 for char in string if 'e' in str(char)]
print(sum(result))