sizeOfList = int(input("Enter the no of tuples in the list: "))
sizeOfTuple = int(input("Enter the no of elements in each tuple: "))
List = []
for i in range(sizeOfList):
    print("Enter the elements in Tuple", i + 1)
    Tuple = []
    for j in range(sizeOfTuple):
        Tuple.append(int(input("Enter the element " + str(j + 1) + ": ")))
    List.append(tuple(Tuple))
N = int(input("Enter the Nth index of sort the list: "))
List.sort(key = lambda x : x[N])
print("sorting tuple List by Nth index sort:",List)
