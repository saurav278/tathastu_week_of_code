size = int(input("Enter the no of words in dictonary: "))
dict = []
for i in range(size):
    dict.append(input("Enter the word " + str(i + 1) + ": "))
size = int(input("Enter the no of character in array: "))
array = []
result = []
print("Enter the characters in array")
for i in range(size):
    array.append(input())
for word in dict: 
    if set(word).issubset(set(array)):
        result.append(word)
print(", ".join(result) + ".")
