def is_even_l(n,k):
    l=n-k+1
    r=n
    if l%2==0:
        odd=l+1
    else:
        odd=l
    if r%2==0:
        e_odd=r-1
    else:
        e_odd=r
    if odd>e_odd:
        count=0
    else:
        count=(e_odd-odd)//2+1
    if count%2==0:
        return "YES"
    else:
        return "NO"        
        

t=int(input())
for i in range(t):
    n,k = map(int, input().split())
    print(is_even_l(n,k))