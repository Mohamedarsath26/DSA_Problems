# Enter the number:4
# ****
# ***
# **
# *

n = int(input("Enter the number:"))
x = n
for i in range(n):
    for j in range(1,x+1):
        print("*",end='')
    x-=1
    print("\n",end='')


