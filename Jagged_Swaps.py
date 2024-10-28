def is_jagged(b, a):
    if arr[0]!=1:
        return "NO"
    else:
        return "YES"  

t = int(input())
for _ in range(t):
    perm = int(input())  
    arr = list(map(int, input().split()))
    print(is_jagged(perm,arr))