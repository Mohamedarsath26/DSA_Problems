arr = [2,3,7,8,1,4]

n = len(arr)

for i in range(n):
    min_val = i
    for j in range(i+1,n):
        if (arr[j] < arr[min_val]):
            min_val = j
    temp = arr[min_val]
    arr[min_val] = arr[i]
    arr[i] = temp

print(arr)