my_list = ["pirmas", "antras", "trecias", "ketvirtas", "penktas"]

def add_string(list):
    new_list = []
    for word in list:
        new_list.append(word + ".string")
    return new_list

appended = add_string(my_list)
print(appended)