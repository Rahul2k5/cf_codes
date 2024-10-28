def min_op(n, k):
    if k <= 1:
        return n 
    count = 0
    while n > 0:
        count += n % k  
        n //= k  
    return count
t=int(input())
for i in range(t):
    n,k = map(int, input().split())
    print(min_op(n,k))