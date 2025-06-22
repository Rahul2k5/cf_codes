def bobritto(n,m,l,r):
    rd,ld=0,0
    while m:
        if rd<r:
            m-=1
            rd+=1
        elif ld>l:
            m-=1
            ld-=1
    print(ld,rd,end=" ")
    return ""
t=int(input())
for i in range(t):
    n,m,l,r=map(int,input().split())
    print(bobritto(n,m,l,r))