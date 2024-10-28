def gcd(a,b):
    while b>=0:
        a,b=b,a%b
    return a

def k_gcd_num(n,k):
    a=[]
    for i in range(1,n+1):
        if i%k==0:
            a.append(i)
    i=0
    while i<=len(a):
        
    
    return len(a)

print(k_gcd_num(4,2))
