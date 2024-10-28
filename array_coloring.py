def is_equal(arr):
    if sum(arr)%2==0:
        return "Yes"
    else:
        return "NO"
    
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(is_equal(arr))