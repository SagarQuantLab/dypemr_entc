# define intial list
initialList = ["a", "b", "c", "b"]

# using for loop
indexList = []
j=0
for i in initialList:
    if i == "b":
        indexList.append(j)
    j = j+1
print(indexList)

# using for loop enumerate
from datetime import datetime

startTime = datetime.now()
indexList = []
for iIndex, jValue in enumerate(initialList):
    if jValue == "b":
        indexList.append(iIndex)
        print("The value of b found at index :", iIndex)
print(indexList)
endTime = datetime.now()

print(endTime - startTime)

# using list index
initialList.index("b")

def returnIndexOfString(stringList, stringToSearch):
    indexList = []
    for iIndex, jValue in enumerate(stringList):
        if jValue == stringToSearch:
            indexList.append(iIndex)
    return indexList

returnIndexOfString(initialList, 'b')