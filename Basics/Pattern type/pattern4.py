# Enter the integer:4
# 1
# 22
# 333
# 4444

n = int(input("Enter the integer:"))

for i in range(1,n+1):
    for j in range(0,i):
        print(i,end='')
    print()
