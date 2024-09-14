## bubble sort

arr = [8,2,5,9,1,3]
n = len(arr)
for i in range(n-1,0,-1):
    print("i",i)
    for j in range(0,i):
        print("j",j)
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
        else:
            continue

print(arr)
