def eff_missing_team(arr):
    x=0
    for i in range(len(arr)):
        x+=arr[i]
    return -x
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(eff_missing_team(arr))