def treasure(x,y,a):
    z=a//(x+y)
    hn=a-z*(x+y)
    if hn+0.5>x:
        return "YES"
    else:
        return "NO"
t=int(input())
for i in range(t):
    x,y,a=map(int,input().split())
    print(treasure(x,y,a))

