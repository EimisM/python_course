my_tuple1 = (1, 2, 3, 4, 5)
my_tuple2 = (6, 7, 8, 9, 10)

# Sum up two lists into one
my_tuple3 = list(map(sum,zip(my_tuple1,my_tuple2)))

# Sum up the values in the new list
print(sum(my_tuple3))