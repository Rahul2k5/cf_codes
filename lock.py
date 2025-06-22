def lock(n):
    if n%2==0:
        return -1
    for i in range(1,n+1,2):
        print(i,end=" ")
    for i in range(2,n+1,2):
        print(i,end=" ")
    return ""
t=int(input())
for i in range(t):
    n=int(input())
    print(lock(n))