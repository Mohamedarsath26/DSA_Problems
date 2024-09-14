# Enter the number4
#     *
#    ***
#   *****
#  *******
def nStarTriangle(n: int) -> None:

    # Initialise 'gap' and 'stars'.
    gap = n - 1
    stars = 1
    for i in range(n):
        for j in range(gap):
            print(' ', end="")
        for j in range(gap, gap+stars):
            print('*', end="")

        # End the current row of the pattern.
        print()

        gap -= 1
        stars += 2

nStarTriangle(5)