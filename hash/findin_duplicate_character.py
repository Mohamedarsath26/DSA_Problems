string = (input("Enter the string:"))
n = len(string)
ch_arr = [0]*256
for i in range(n):
    ch_arr[ord(string[i])]+=1
query = int(input())
for _ in range(query):
    ch = input()
    print(ch_arr[ord('a')])
