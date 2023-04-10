number ="9,223,113,134,422,414,144"
separators = ""
for char in number:  #goes through every character one by one
    if not char.isnumeric():
        separators = separators + char

print(separators)

print("*"*80)

num = input("Enter a number: ")
sep = ""
for f in num:
    if not f.isnumeric():
        sep = sep + f
print(sep)