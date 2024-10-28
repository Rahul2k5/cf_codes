def unit_Arr(arr):
    a = 0
    b = 0 
    sum_arr = 0 
    for i in arr:
        if i==1:
            a+=1
        else:
            b+=1
        sum_arr+=i 
    if sum_arr>=0 and b%2==0:
        return 0
    else:
        x=0
        while sum_arr<0:
            sum_arr+=2
            b-=1 
            x+=1
        if b%2!=0:
            x+=1
        return x

t = int(input())
for i in range(t):
    n = int(input())  
    arr = list(map(int, input().split()))  
    print(unit_Arr(arr))
