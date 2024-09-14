# Enter n:4
# A
# AB
# ABC
# ABCD
#method 1
n = int(input("Enter n:"))
for i in range(65,65+n):
    for j in range(65,i+1):
        print( chr(j),end='')
    print()


#method 2
n = int(input("Enter n1:"))
for i in range(n):
    ch = ord('A')
    for j in range(i+1):
        print(chr(ch),end='')
        ch = ch+1
    print()