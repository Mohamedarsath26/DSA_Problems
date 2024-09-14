n = int(input("Enter the number:"))
arr = []
for i in range(n):
    x = int(input("Enter the i number:"))
    arr.append(x)
print(arr)

hash = [0]*13
que = int(input("Enter the number of queries:"))

for i in range(n):
    hash[arr[i]] += 1

while(que):
    x = int(input("Enter the number"))
    print(hash[x])
    que = que-1
else:
    print("Finshed")