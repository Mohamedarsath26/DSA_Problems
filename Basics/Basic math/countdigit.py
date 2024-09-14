n = int(input("Enter integer:"))
count = 0
x = n
while(x>0):
    x = x//10
    count+=1
print("No of digit is:",count)