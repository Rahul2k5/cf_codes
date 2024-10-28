def is_coin(n,k):
        if(n%k == 0 or n%2 == 0):
            return "YES"
        elif((n-2) %k == 0 or (n+2) % k == 0):
            return "YES"
        elif((n-k) % 2 == 0 or (n+k) % 2 == 0):
            return "YES"    
        return "NO"
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    print(is_coin(n,k))
