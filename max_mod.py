def max_mod(n):
    if n%2==0:
        return -1
    print(n,end=" ")
    for i in range(1,n):
        print(i,end=" ")
    return ""
t=int(input())
for i in range(t):
    n=int(input())
    print(max_mod(n))