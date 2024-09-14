# Enter n :4
#    A
#   ABC
#  ABCDC
# ABCDEDC
n = int(input("Enter n :"))
gap = n-1
ch = 1
for i in range(n):
    for j in range(gap):
        print(" ",end='')
    pp = int(2*i+1)//2
    let = ord('A')
    for j in range(2*i+1):
        print(chr(let),end='')
        if (j<pp):
            let+=1
        else:
            let-=1
    gap-=1
    ch+=2
    print()

