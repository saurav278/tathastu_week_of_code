def sort(List):
    odd = []
    even = []
    for x in List:
        if x % 2 == 0:
            even.append(x)
        else :
            odd.append(x)
    return sorted(odd, reverse = True) + sorted(even)
size = int(input("Enter the number of elements in the array: "))
List = []
for i in range(size):
    List.append(int(input("Enter the element number " + str(i + 1) + " in the list: ")))
print("sorting them according to given condition is", str(sort(List))[1:-1])
