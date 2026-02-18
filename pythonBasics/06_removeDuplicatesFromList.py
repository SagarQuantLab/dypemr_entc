# initial list
initialList = ['a', 'b', 'c', 'a', 'b', 'd']

# using for loop
uniqueList = []
for i in initialList:
    if i not in uniqueList:
        uniqueList.append(i)

print(uniqueList)

# using sets - Drawback - order is not maintained
print(list(set(initialList)))

# using dictionary
print(list(dict.fromkeys(initialList)))

# using order dictionary
from collections import OrderedDict
print(list(OrderedDict.fromkeys(initialList)))