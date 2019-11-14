full_name = ""
first = input("What is your first name? \n")
middle = input("What is your middle name?\n")[0].upper()
last = input("What is your last name? \n")
full_name = first + " " + middle + ". " + last

print("Hello, " + full_name + ".")
print(first[0] + "." + last[0] + ".")

print(first[0:len(first)-1] + first[len(first)-1].upper())
# String[Index] returns letter, starts at 0.
# "word"[1] == o

#variable[startIndex:endIndex] -- prints the letters from start to end [NOT including end]
#"word" == wor

