def cost(k,arr):
    if k in arr:
        return "YES"
    else:
        return "NO"

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int, input().split()))
    print(cost(k,arr))