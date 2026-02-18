# how to reverse a string
# 1. Using indexing
# 2. Using for loop
# 3. Using reverse and join 

my_string  = "hello friend this is ENTC students"

# 1
reveresed_string = my_string[::-1]

# 2
reveresed_string = ""
for each_char in my_string:
    reveresed_string = each_char + reveresed_string

# 3
reveresed_string = "".join(reversed(my_string))
print(reveresed_string)