n = int(input("Enter the number:"))
##functional way
def sum_of_n(n):
    if(n==0):
        return 0
    return n + sum_of_n(n-1)

##parameterized way
def sum_of_n1(n,sum):
    if(n<1):
        print(sum)
        return
    return sum_of_n1(n-1,sum+n)
sum_of_n1(n,0)
