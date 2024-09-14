n = int(input("Enter the number:"))
arr = []
for i in range(n):
    x = int(input("Enter the number:"))
    arr.append(x)

hash = [0]*21
query = []
for i in range(n):
    hash[arr[i]] += 1
q = int(input("Enter the no of query:"))
for i in range(q):
    query.append(int(input()))
for i in range(q):
    print(query[i], hash[query[i]])
