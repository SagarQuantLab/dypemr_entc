# # string and its operation
# my_string = "Hello this is College"
# print(my_string)

# # print string reverse
# reverse_string = my_string[::-1]
# print(reverse_string)

# # access first element
# print(my_string[0])
# print(my_string[1])
# print(my_string[0:3])
# print(my_string[6:10])
# print(my_string[:-4:-1])
# print(my_string.count('H'))
# print(my_string*10)
# print(my_string.replace("H", "Z"))
# print(my_string.lower())
# print(my_string.upper())

# # list & its operation
# my_list = ["Apple", "Banana", "orange"]
# # print(my_list[0])
# # print(my_list[0:2])
# # my_list.append("Guava")
# # print(my_list)
# # my_list.pop()
# # print(my_list)

# my_list2 = ["Grapes", "Mango"]

# # what is the differenc between append and extend in list?
# print(my_list)
# my_list.append(my_list2)
# print(my_list)
# my_list = ["Apple", "Banana", "orange"]
# my_list.extend(my_list2)
# print(my_list)
# my_list.sort()
# print(my_list)
# print(my_list.pop(0))
# print(my_list)


########################
# how to create dictionary from two lists?
my_dict = {
    "Name": "Rohan",
    "Age" : 35,
    "Gender" : "M"
}

print(my_dict["Name"])
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
my_dict["Age"] = 18
print(my_dict)
my_dict.update({"Religion" : "Hindu"})
print(my_dict)
my_dict.pop("Gender")
print(my_dict)