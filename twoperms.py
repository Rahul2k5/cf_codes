def two(n,a,b):
    if n==a==b:
        return "YES"
    if n-(a+b)>1:
        return "YES"
    else:
        return "NO"
t=int(input())
for i in range(t):
    n,a,b=map(int,input().split())
    print(two(n,a,b))