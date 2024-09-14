# Enter n:4
# ********
# ***  ***
# **    **
# *      *
# *      *
# **    **
# ***  ***
# ********

n = int(input("Enter n:"))
star = n-1
gap = 0
for i in range(n):
    ##stars
    for j in range(1,n-i+1):
        print("*",end='')
    ##space
    for j in range(gap):
        print(" ",end='')
    ##stars
    for j in range(1,n-i+1):
        print("*",end='')


    gap=gap+2

    print()

star1 = 1
gap1 = 2*n-2
for i in range(n):
    ##stars
    for j in range(i+1):
        print("*",end='')
    ##space
    for j in range(gap1):
        print(" ",end='')
    ##stars
    for j in range(i+1):
        print("*",end='')

    star1 = star1+1
    gap1 = gap1-2
    print()
