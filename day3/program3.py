def dup(string):
    dupString = ""
    for x in string:
        if x not in dupString:
            dupString += x
    return dupString

string = input("Enter the string: ")
print("After removing the duplicates is:", dup(string))

