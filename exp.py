def expensive(a):
    wei=0
    n=len(a)
    a = ' ' + a
    for i in range(n, 0, -1):
        if a[i] != '0':
            wei = i
            break
    ans = 0
    for i in range(1, wei):
        if a[i] != '0':
            ans += 1
    ans += n - wei
    return ans 
t=int(input())
for i in range(t):
    n=str(input())
    print(expensive(n))