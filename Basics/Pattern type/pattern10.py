# Enter the number:4

#
# *
# **
# ***
# ****
# ***
# **
# *

n = int(input("Enter the number:"))
stars = 0
def half_diamond(n):
    for i in range(2*n):
        stars = i
        if(i>n):
            stars = 2*n-i
        for j in range(stars):
            print("*",end='')
        print()

half_diamond(n)