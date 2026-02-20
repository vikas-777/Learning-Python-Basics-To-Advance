my_dict = {"name": "vikas", "age": 21, "job": "no", "contact": 9533666836}
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
for x in my_dict:
    print(x, end=" ")
# print(f"\n")
for y in my_dict.values():
    print(y, end=" ")
# print(f"\n")
for i in my_dict.keys():
    print(i, end=" ")
# print(f"\n")
if "vikas" in my_dict.values():
    print("\nalive")
else:
    print("\ndead")
if "age" in my_dict:
    print("vikas is good boy")
else:
    print("vikas is bad boy")
for a, b in my_dict.items():
    print(a, ":", b)
dict1 = {"name": "vikas"}
dict2 = {"age": 21}
dict1.update(dict2)
print(dict1)
my_dict.popitem()         #last element contact is removed
print(my_dict)
my_dict.pop("age")
print(my_dict)
my_dict["job"]="yes"
print(my_dict)
copy_my_dict = my_dict
print(copy_my_dict)
