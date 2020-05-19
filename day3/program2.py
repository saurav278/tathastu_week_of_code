def per(List, Str = ""):
    Set = set(List)
    strList = []
    if len(Set) == 1:
        Str += "".join(List)
        return list([Str])
    for x in Set:
        List1 = list(List)
        S = Str + x
        List1.remove(x)
        strList.extend(per(List1, S))
    return strList

str = input("Enter a string: ")
List = per(list(str))
print("All the permutation of given string is: " + ", ".join(List))
