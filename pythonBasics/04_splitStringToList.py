# define initial string
initialString = "Hello World this is JLR"

# split string based on some char
print(initialString.split('l'))

# split string based on space
print(initialString.split())

# limiting the number of splits
print(initialString.split(" ",2))

# splitting a string into characters
newList = list(initialString)
print(newList)

# join list of string in a single string
print("".join(newList))