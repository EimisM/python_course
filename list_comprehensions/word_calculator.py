text = 'In this lecture we will review some additional functionalities of python built-in data structures'
string = text.split(" ")
result = [1 for word in string if len(word) >= 5]
print(sum(result))