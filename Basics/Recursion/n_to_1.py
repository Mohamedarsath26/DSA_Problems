n = int(input("Enter number:"))
def num_to_1(n,i):
    if(n<1):
        return
    else:
        print(n)
        num_to_1(n-1,i)

num_to_1(n,1)