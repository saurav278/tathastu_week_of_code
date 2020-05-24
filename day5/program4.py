def knapsack(n, w):
    if n == 0 or len(w) == 0:
        return 0
    if len(w) == 1:
        if w[0][0] > n:
            return 0 
        return w[0][1]  
    if w[0][0] > n:
        return knapsack((n, w[1:]))
    return max(w[0][1] + knapsack(n - w[0][0], w[1:]), knapsack(n, w[1:]))
size =  int(input("Enter the number of items: "))
w = []
for i in range(size):
    n = int(input("Enter the weight for item number " + str(i + 1) + ": "))
    value = int(input("Enter the value for item number " + str(i + 1) + ": "))
    w.append((n,value))
n = int(input("Enter the value of weight capacity: "))
print("The maximum value of weight value pair is ", knapsack(n, w))
