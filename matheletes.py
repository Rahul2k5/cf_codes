def game_of_mathletes(n, k, x):
    x.sort()  
    l, r = 0, n - 1
    a = 0
    while l < r:
        s = x[l] + x[r]
        if s == k:
            a += 1
            l += 1
            r -= 1
        elif s < k:
            l += 1
        else:
            r -= 1
    print(a)

t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    game_of_mathletes(n, k, x)
