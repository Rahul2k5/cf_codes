def amb_kid(arr):
    return min(arr)
n=int(input())
arr=list(map(int,input().split()))
for i in range(len(arr)):
    if arr[i]<0:
        arr[i]=arr[i]*(-1)
print(amb_kid(arr))
