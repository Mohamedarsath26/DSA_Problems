# Enter n :4
# A
# BB
# CCC
# DDDD

n = int(input("Enter n :"))
for i in range(n):
    ch = ord('A')
    ch = ch+i
    for j in range(i+1):
        print(chr(ch),end='')
    print()

