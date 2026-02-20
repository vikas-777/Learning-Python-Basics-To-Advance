d = {"fruits":{"apple":"red"},"flowers":{"lilly":"pink"},"vegetables":{"potato":"brown"}}

print("1",d["flowers"]["lilly"])
for x,y in d.items():
    print("2",x,">>>",y)
for x,y in d.items():
    for z in y:
        # print("3",z,":",y[z])
        print("colour --",y[z])
set1 = "vikas"
set2 = "atapakala"
set3 = "beginner"
myset = {set1, set2, set3} #using name as set but creating (keys)dictionary
myDict = {set1:"name",set2:"surname",set3:"proficiency"}
for i in myDict.items():
    print(i)
