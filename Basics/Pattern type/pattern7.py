# Enter the number4
#     *
#    ***
#   *****
#  *******


n = int(input("Enter the number"))
for i in range(1,n+1):
    for j in range(2*n-1+1):
        if ( j>= n-(i-1) and j<= n+(i-1)):
            print("*",end='')
        else:
            print(" ",end='')
    print('\n',end='')


