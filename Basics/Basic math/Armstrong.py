n = int(input("Enter the number:"))
##finding digit
digit = 0
x=n
while(x!=0):
    x = x//10
    digit+=1
## for finding Armstrong
x1 = n
rem = 0
sum = 0
while(x1!=0):
    rem = x1%10
    sum = sum + pow(rem,digit)
    x1 = x1//10
if (sum==n):
    print("This is armstrong")
else:
    print("This is not armstrong")
