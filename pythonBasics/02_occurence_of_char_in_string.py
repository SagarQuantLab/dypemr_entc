my_string = "This is DYPEMR ENTC"

print(my_string.count('E'))


############# count char in string using COUNTER
from collections import Counter
char_to_search = 'l'
count = Counter(my_string)
print(count(char_to_search))