# Enter the number:4
# *******
#  *****
#   ***
#    *
def nStarTriangle(n):
 # Initialise 'gap' and 'stars'.
    gap = 0
    stars = 2*n-1
    for i in range(n):
        for j in range(gap):
            print(' ', end="")
        for j in range(gap, gap+stars):
            print('*', end="")

        # End the current row of the pattern.
        print()
        gap += 1
        stars -= 2


n = int(input("Enter the number:"))
nStarTriangle(n)