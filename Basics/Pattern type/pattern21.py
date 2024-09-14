# Enter the number:4
# ****
# *  *
# *  *
# ****
n = int(input("Enter the number:"))
for i in range(n):
    if (i == 0 or i == n-1):
        for j in range(n):
            print("*",end='')
    else:
        star = 1
        gap = n-2
        for j in range(star):
            print("*",end='')
        for j in range(gap):
            print(" ",end='')
        for j in range(star):
            print("*",end='')

    print()