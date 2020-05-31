def seg(arr, size): 
    j = 0
    for i in range(size): 
        if (arr[i] <= 0): 
            arr[i], arr[j] = arr[j], arr[i] 
            j += 1 
    return j  

def MissingPositive(arr, size): 
      

    for i in range(size): 
        if (abs(arr[i]) - 1 < size and arr[abs(arr[i]) - 1] > 0): 
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1] 
 
    for i in range(size): 
        if (arr[i] > 0): 

            return i + 1
    return size + 1

def Missing(arr, size): 
      

    shift = seg(arr, size) 

    return MissingPositive(arr[shift:], size - shift)   
arr = [ 0, 10, 2, -10, -20 ] 
arr_size = len(arr)  
missing = Missing(arr, arr_size)  
print("The smallest positive missing number is ", missing)
