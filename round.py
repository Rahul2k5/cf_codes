def round(n):
    count=0
    for i in range(1,n+1):
        if i<10:
            count+=1
    
t=int(input())
for i in range(t):
    n=int(input())
    print(round(n))
