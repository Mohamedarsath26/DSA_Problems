# enter number:4
# *
# **
# ***
# ****

n = int(input("enter number:"))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end='')
    print("\n",end='')