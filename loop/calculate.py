inputlist = []
while True:
    num = int(input("Please insert a number "))
    inputlist.append(num)
    if len(inputlist) == 10:
        break

combined = sum(inputlist)
average = combined / len(inputlist)

print(f"{combined}")
print(f"{average}")