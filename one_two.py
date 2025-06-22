def one_two(arr):
    count=0
    for i in arr:
        if i==2:
            count+=1
    if count==0:
        return 1
    if count%2==1:
        return -1 
    else:
        x=0
        for i in range(len(arr)):
            if arr[i]==2:
                x+=1
                if x==count//2:
                    return i+1
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(one_two(arr))