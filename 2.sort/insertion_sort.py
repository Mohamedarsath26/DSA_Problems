arr = [5,3,1,7,8,10]

n = len(arr)

for i in range(n):
    j = i ## pick the first element 
    print("j",arr[j])
    while(j>0 and arr[j-1]>arr[j]):
        
        arr[j-1],arr[j] = arr[j],arr[j-1] ## check with left side element if it is greater swap it.

        j-=1 ## decrement the number
        
print(arr)