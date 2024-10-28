
def need_zero(a,n):
    t = 0
    for i in a:
        t ^= i
    if n % 2 == 0 and t > 0:
        return -1
    else:
        return t

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    print(need_zero(a,n))