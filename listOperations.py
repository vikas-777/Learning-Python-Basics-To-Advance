My_list = ["apple", "ball", "cat", "dog", "elephant"]
print("1", My_list)
Num_list = [13, 22, 6, 56, 34]
Num_list.sort()
print("2", Num_list)
Num_list.reverse()
print("3", My_list)
My_list.append(Num_list)
print("4",My_list)
My_list.insert(5, "bye")
print("5", My_list)
My_list.pop(1)
print("6", My_list)
My_list.remove(Num_list)
print("7", My_list)
My_list.reverse()
print("8", My_list)
My_list.append(Num_list)
print("9", My_list)
print("10", Num_list)

for name in My_list:
    print("11",name)
My_list.remove(Num_list)
print("12",My_list, " here im removing num list because it has integers we cant add strings to them")

for name in My_list:
    if name == "dog":
        print("13",name + " jaggu 6093")

for name in My_list:
    if name == "dog":
        print(f"14 {name} jaggu 6093")
    else:
        print(f"14 {name} are Strings")
print("15",My_list.pop(3),"<<<str in index 3 is poped")

print("16",My_list)
for name in My_list:
    if name == "apple":
        print(name," you can come inside")
    else:
        print(f"{name} you cant come inside")
if "apple" in My_list:
    print("apple exists in the list ")
else:
    print("apple not exists in list")
print(f"prints element at index -3 {My_list[-3]}")
print(f"prints element at index 1 {My_list[1]}")

print(type(My_list))
print(type(Num_list))
My_list.sort()
print(My_list)