# Enter n :4
# ABCD
# ABC
# AB
# A
n = int(input("Enter n :"))
for i in range(n):
    ch = ord('A')
    for j in range(i,n):
        print(chr(ch),end='')
        ch = ch+1
    print()

