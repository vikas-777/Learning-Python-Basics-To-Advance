string1 = ["apple","ball","cat","dog","egg"]
string2 = []
for i in string1:
    if "a" in i:
        string2.append(i)
print(string2)
##################################
string2 = [i for i in string1 if "a" in i]
print(string2)
######################################
