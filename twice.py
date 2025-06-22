def score(arr):
    a = {}
    ans = 0
    for i in arr:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    for i in a.values():
        ans += i // 2
    return ans

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(score(arr))
