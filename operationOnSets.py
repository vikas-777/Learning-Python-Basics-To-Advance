# Sets: Sets are a collection of unique elements.
# They are unindexed. Unordered.
# immutable
mySet = {"red", "blue", "green","amber", "black"}
print(mySet)
# print(len(mySet))
# print(type(mySet))
# access set items
# for color in mySet:
#     print(color)
# print("red" in mySet)
# print("red" not in mySet)
# if "red" in mySet:
#     print("Exists")
# else:
#     print("Not Exists")
# # update the set
# mySet.add("pink")
# print(mySet)
mySet2 = {"amber", "cyan", "indigo"}
print(mySet.intersection(mySet2))
mySet.update(mySet2)
print(mySet)
myList = ["black", "white"]
mySet.update(myList)
print(mySet)
mySet.remove("amber")
print(mySet)
# mySet.discard("black")
# print(mySet)
print(mySet)
mySet.pop()
print(mySet)
# List = {
#         "num1":10,
#         "num2":11,
#         "num3":0
#         }
# List.popitem()
# print(List)
# mySet.clear()
# del mySet
# print(mySet)
set1 = {"good", "better", "best"}
set2 = {"worse", "poor", "worst", "good"}
set3 = set1.union(set2)
print(set3)
set4 = set1.intersection(set2)
print(set4)
# # items that are not in other sets
set5 = set2.difference(set1)
# # set6 = set1.add(set2)
print(set5)
# # keeps all except duplicates
set6 = set1.symmetric_difference(set2)
print(set6)
# # joins
overall = set1 | set2
print(overall)