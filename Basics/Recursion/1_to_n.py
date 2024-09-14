# n = int(input("Enter the number:"))
# def name(i,n):
#     if(i>n):
#         return
#     else:
#         print(i)
#         name(i+1,n)

# name(1,n)

n = int(input("Enter the number:"))

def name1(i,n):
    if(i>n):
        return
    else:
        print(i)
        name1(i+1,n)

name1(1,n)


