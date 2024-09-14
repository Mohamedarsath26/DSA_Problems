# Enter the integer:4
# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444
n = int(input("Enter the integer:"))
elem = n
n1 = 1
m1 = n
for i in range((2*n)-1):
    for j in range((2*n)-1):
        top = i
        bot = (2*n)-2-i
        left = j
        right = (2*n)-2-j
        print(n-min(min(top,bot),min(left,right)),end='')
    print()
