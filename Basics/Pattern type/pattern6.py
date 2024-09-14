# Enter the number:4
# 1234
# 123
# 12
# 1
n = int(input("Enter the number:"))
x = n
for i in range(n):
    for j in range(1,x+1):
        print(j,end='')
    x-=1
    print()