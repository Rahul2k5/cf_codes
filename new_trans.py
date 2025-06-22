def new(n):
    count = 1
    while n > 3:
        n //= 4
        count *= 2
    return count
t=int(input())
for i in range(t):
    n=int(input())
    print(new(n))