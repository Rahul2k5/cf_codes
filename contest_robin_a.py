def gold(n,k,arr):
    ans=0
    x=0
    for i in range(n):
        if k<=arr[i]:
            x+=arr[i]
        elif arr[i]==0 and x>0:
                ans+=1
                x-=1
    return ans

t=int(input())
for i in range(t):
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(gold(n,k,arr))