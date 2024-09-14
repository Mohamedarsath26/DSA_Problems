#User function Template for python3

#Function to sort a list using quick sort algorithm.
def quickSort(arr,low,high):
    if (low<high):
        p_index = partition(arr,low,high)
        quickSort(arr,low,p_index-1)
        quickSort(arr,p_index+1,high)

    return arr
            
def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    while(i<j):
        while(arr[i]<=pivot and i<=high-1):
            i+=1
        while(arr[j]>pivot and j>=low+1):
            j-=1
        if(i<j):
            arr[i],arr[j] = arr[j],arr[i]
        else:
            break
        
    arr[low],arr[j] = arr[j],arr[low]
    return j

arr = [4,5,6,1,2,3]
print(quickSort(arr,0,len(arr)-1))