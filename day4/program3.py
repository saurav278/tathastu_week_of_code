size = int(input("Enter the no of items you want to add in Dictonary: "))
new_dict = dict()
for i in range(size):
    key = input("Enter the key for item " + str(i + 1) + " in dictonary: ")
    value = int(input("Enter the value for item " + str(i + 1) + " in dictonary: "))
    new_dict[key] = value



max = max(new_dict.values()) 
max2 = 0
for v in new_dict.values(): 
     if(v>max2 and v<max): 
            max2 = v 
  

print(max2) 
