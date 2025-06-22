def train(m,arr):
    arr.sort(reverse=True)
    count=0
    count2=0
    x=float("inf")
    for i in range(len(arr)):
        count2+=1
        x=min(arr[i],x)
        if count2*arr[i]>=m:
            count+=1
            count2=0
    return count
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    print(train(m,arr))