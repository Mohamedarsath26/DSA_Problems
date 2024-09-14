def print_arr(arr,n):
    for i in range(n):
        print(arr[i],end='')

def reverse_arr(arr,start,end):
    if(start<end):
        arr[start],arr[end] = arr[end],arr[start]
        return reverse_arr(arr,start+1,end-1)


arr = [1,2,3,4,5]
n = len(arr)
reverse_arr(arr,0,n-1)
print_arr(arr,n)