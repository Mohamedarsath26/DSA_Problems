n=int(input("Enter integer:"))
digit = 0
reverse = 0
x=n
while(x!=0):
    digit = x%10
    reverse = reverse*10 + digit
    x = x//10

print("Reverse of a number is:",reverse)