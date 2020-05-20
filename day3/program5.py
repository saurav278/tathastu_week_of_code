s1 = int(input("Enter the no of elements in the List 1: "))
print("Enter the elements in List1")
list1 = []
for i in range(s1):
    list1.append(input())
s2 = int(input("Enter the no of elements in the List 2: "))
print("Enter the elements in List2")
list2 = []
for i in range(s2):
    list2.append(input())
intersectionList = list(set(list1).intersection(set(list2)))
print("The intersection of List 1 and List 2 is:", ", ".join(intersectionList))
