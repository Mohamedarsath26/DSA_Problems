# Enter the number:4
# *      *
# **    **
# ***  ***
# ********
# ***  ***
# **    **
# *      *
n = int(input("Enter the number:"))
star = 1
gap = 2*n-2
for i in range(2*n-1):
    for j in range(star):
        print("*",end='')
    ##space
    for j in range(gap):
        print(" ",end='')
    ##star
    for j in range(star):
        print("*",end='')
    if(i>=n-1):
        star -= 1
        gap += 2
    else:
        star+=1
        gap-=2
    print()