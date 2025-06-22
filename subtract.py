def sub():
    n = int(input().strip())
    a = list(map(int, input().split()))
    for i in range(n - 1):
        if a[i] <= a[i + 1]:
            temp = a[i]
            a[i] = 0
            a[i + 1] -= temp
    ok = all(a[i] <= a[i + 1] for i in range(n - 1))
    print("YES" if ok else "NO")

t = int(input().strip())
for i in range(t):
    sub()
