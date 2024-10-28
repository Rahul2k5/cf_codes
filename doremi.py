def doremi(arr):
    a={}
    for i in arr:
        if i in a:
            a[i]+=1
        else:
            a[i]=1  
    if len(a)==1:
        return "YES"
    if len(a)>2:
        return "NO"
    counts=list(a.values())

    if abs(counts[0]-counts[1])<=1:
        return "YES"
    else:
        return "NO" 

t=int(input())
for i in range(t):
    n = int(input())  
    arr = list(map(int, input().split()))
    print(doremi(arr))