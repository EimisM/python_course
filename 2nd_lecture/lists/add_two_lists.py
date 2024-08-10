my_list1 = [1, 2, 3, 4, 5]
my_list2 = [6, 7, 8, 9, 10]

# Sum up two lists into one
my_list3 = list(map(sum,zip(my_list1,my_list2)))

# Sum up the values in the new list
print(sum(my_list3))