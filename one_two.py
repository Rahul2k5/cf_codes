def one_two(arr,n):
    total = 1
    for i in arr:
        total *= i
    l_sum = 1
    for i in range(n-1):
        l_sum *= arr[i] 
        r_sum = total // l_sum  
        if l_sum == r_sum:
            return i+1
    return -1 

t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(one_two(arr,n))