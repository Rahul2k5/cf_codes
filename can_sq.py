def can(arr):
    x=sum(arr)
    l=0
    r=x
    while l<=r:
        m=(l+r)//2
        if m*m==x:
            return "yes"
        elif m*m<x:
            l=m+1
        else:
            r=m-1
    return "NO"
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(can(arr))