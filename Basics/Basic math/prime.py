n = int(input("Enter the number:"))
count = 0
for i in range(2,n):
    if(n%i==0):
        flag = True
        break
    else:
        flag = False

if(flag):
    print("This not prime number")
else:
    print("This is prime number")


