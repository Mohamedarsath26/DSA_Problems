# Enter the number:4
#    *
#   ***
#  *****
# *******
# *******
#  *****
#   ***
#    *

def nStarTriangle(n: int) -> None:
    # Initialise 'gap' and 'stars'.
    gap = n - 1
    stars = 1
    for i in range(n):
        for j in range(gap):
            print(' ', end="")
        for j in range(gap, gap + stars):
            print('*', end="")

        # End the current row of the pattern.
        print()

        gap -= 1
        stars += 2

 # Initialise 'gap' and 'stars'.
    gap1 = 0
    stars1 = 2*n-1
    for i in range(n):
        for j in range(gap1):
            print(' ', end="")
        for j in range(gap1, gap1+stars1):
            print('*', end="")

        # End the current row of the pattern.
        print()
        gap1 += 1
        stars1 -= 2

n = int(input("Enter the number:"))
nStarTriangle(n)