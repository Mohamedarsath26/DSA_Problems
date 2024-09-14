low_high = dict({})
def countFreq(arr, n):
    visited = [False] * n
    for i in range(n):
        if (visited[i] == True):
            continue
        count = 1
        for j in range(i + 1, n):
            if (arr[i] == arr[j]):
                visited[j] = True
                count += 1
        print(arr[i], count)
        low_high.update({arr[i]:count})

    Key_max = max(zip(low_high.values(), low_high.keys()))[1]
    print(Key_max)
    Key_min = min(zip(low_high.values(), low_high.keys()))[1]
    print(Key_min)
if __name__ == "__main__":
    arr = [10,5,10,15,10,5]
    n = len(arr)
    countFreq(arr, n)

