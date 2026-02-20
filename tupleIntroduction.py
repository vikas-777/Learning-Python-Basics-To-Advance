tple = ("apple", "ball", "20", 40, 60)
print(tple)
tple2 = ("cat","dog","2",4,6)
my_tup = tple+tple2
print(my_tup)
my_tup = list(my_tup)
print(my_tup)
my_tup.remove("cat")
print(my_tup)
for i in my_tup:
    print(i)
for i in my_tup:
    print(i*2)
print(f"type",type(my_tup))
print(f"type",type(tple))
findIndex = tple.index("20")
print(f"index {findIndex}")
tple=tple2
print(tple)
print(tple2)
 # packing and unpacking
(green, yellow, yellow_orange, pink, red) = tple
print(green, yellow, yellow_orange, pink, red)

(green, *yellow, pink, red) = tple
print(green, *yellow, pink, red)
(green, *yellow) = tple
print(green,*yellow)