# lists are collections of stuff

names = ["Sarah", "Amy", "Sean", "Zach"]
print(names)

for i in names:
    print(i)
    
# for i in collection:
    # i is = the elements in the list.

#===============================================================================
# for i in names: # you can modify the list 
#     i += "'s"
#     print(i)
#===============================================================================

names[2] = "Fred"
print(names)
names.remove("Fred")
print(names)
names.append("John")
print(names)
names.sort()
print(names)
names.insert(2, "Keith")
print(names)

