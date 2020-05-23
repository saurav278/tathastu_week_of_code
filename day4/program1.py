size = int(input("Enter the size of tuple: "))
print("Enter the elements in tuple one by one")
a = []
for i in range(size):
    a.append(input())
b = tuple(a)
element = input("Enter the element whose occurrences: ")
print("Tuple contains the element", b.count(element), "times")
