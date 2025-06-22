def sliding(n,m,r,c):
    zhi = 2 * m - 1
    result = zhi * (n - r) + m - c
    return result
t=int(input())
for i in range(t):
    n,m,r,c=map(int,input().split())
    print(sliding(n,m,r,c))