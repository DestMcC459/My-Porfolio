#created a list with 4 strings and print out each on each iteration
values = ["a", "b", "c", "d"]

for count, value in enumerate(values): 
    print(value)

index = 0
# print the index of the item in the list 
for index in range(len(values)): 
    value = values[index]
    print(index, values)
    index += 1


