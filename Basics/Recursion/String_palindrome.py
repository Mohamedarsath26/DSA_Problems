def string_palin(s,start,end):
    if (start>=end):
        return True
    if(s[start]!=s[end]):
        return False
    return string_palin(s,start+1,end-1)

s = "mam"
n = len(s)
print(string_palin(s,0,n-1))

