def count_init(x,s,n,m):
    i=0
    while s not in x:
        if n>m*2 and i>=1:
            return -1
        x+=x
        n*=2
        i+=1
    return i
    

t = int(input())
for _ in range(t):
    n, m= map(int, input().split())
    x = str(input())
    s = str(input())
    print(count_init(x,s,n,m))