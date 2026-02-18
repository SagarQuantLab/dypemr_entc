# define list
list1 = ['a', "b", "c"]
list2 = [1, 2, 3]

# join two list using plus operator
print(list1 + list2)

# join two list using unpacking
print([*list1, *list2])

# join two list using extend
list1.extend(list2)
print(list1)

# using simple bracket operator
print([list1, list2])