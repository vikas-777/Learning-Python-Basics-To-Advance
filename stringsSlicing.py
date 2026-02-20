name = "python programming"
#       0123456789112345678
print(name[0:19])
print(name[-1:0])
# here we don't get any values note "0 is the first char and -1 is the last char of string so no values b/w them"
print(name[0:-5])  # we can do positive to negative slicing also
print(name[7:19:3], ":slicing every 3rd value")
print(len(name))
print(name.endswith("ing"))
print(name.startswith("py"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.find("g"))
print(name.replace("python", "vikas"))  # stores in a new variable
print(name.replace("programming", "vikas"))  # stores in another new variable
print(name[::-1])