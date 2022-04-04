a=input().split()
def rec(a,b):
    if a==0 or b==0:
        return a+b
    if a>b:
        return rec(a%b,b)
    else:
        return rec(b%a,a)
print(rec(int(a[0]),int(a[1])))