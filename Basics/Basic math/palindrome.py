n=int(input("Enter integer:"))
digit = 0
reverse = 0
x=n
while(x!=0):
    digit = x%10
    reverse = reverse*10 + digit
    x = x//10

if(n == reverse):
    print("this is palindrome")
else:
    print("Not palindrome")