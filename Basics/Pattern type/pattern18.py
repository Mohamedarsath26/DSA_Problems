# enter n:4
# D
# CD
# BCD
# ABCD
n = int(input("enter n:"))
ch1 = ord('A')+n-1
ch = ch1
for i in range(n):
    for j in range(ch-i,ch1+1):
        print(chr(j), end='')
    print()


