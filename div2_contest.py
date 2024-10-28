def pair_segments(n,q,x,queries):
    a = {}
    for i in range(1, n + 1):
        k_p = (i - 1) * (n - i + 1) + (n - i)
        a[k_p] = a.get(k_p, 0) + 1
        if i < n:
            diff = x[i] - x[i - 1] - 1
            if diff > 0:
                b = i * (n - i)
                a[b] = a.get(b, 0) + diff
    ans = []
    for i in queries:
        ans.append(str(a.get(i, 0)))
    return ' '.join(ans)

t = int(input())
for i in range(t):
    n, q = map(int, input().split())
    x = list(map(int, input().split()))
    k_list = list(map(int, input().split()))
    print(pair_segments(n, q, x, k_list))
