def fibonacii(n):
    if(n<=1):
        return n
    return fibonacii(n-1) + fibonacii(n-2)


n = int(input("Enter the number to get fibonacci series:"))
print(fibonacii(n))


