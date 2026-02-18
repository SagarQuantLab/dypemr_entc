# how to convert lists into dictionary

key_list = ["Name", "Age", "Gender"]
value_list = ["Rohan", 35, "M"]

# Zip
my_dict = dict(zip(key_list, value_list))
print(my_dict)

# for loop
my_dict = {}

for i, ikey in enumerate(key_list):
    my_dict[ikey] = value_list[i]

i = 0
for ikey in key_list:
    my_dict[ikey] = value_list[i]
    i = i + 1


print(my_dict)