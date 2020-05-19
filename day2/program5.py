N = int(input("Enter the Value of n: "))
for i in range(N):
    print((str(N - i) + "*") * (N - 1 - i) + str(N - i))
for i in range(1,N + 1):
    print((str(i) + "*") * (i - 1) + str(i))   
