from collections import defaultdict
def pair_segments(n, x, k_list):
    covered = defaultdict(int)
    for i in range(n):
        for j in range(i + 1, n):
            covered[x[i]] += 1
            covered[x[j] + 1] -= 1
    cover = 0
    count = defaultdict(int)
    l = 0
    sor_keys = sorted(covered.keys())
    for i in sor_keys:
        if cover > 0:
            count[cover] += i - l
        cover += covered[i]
        l = i
    ans = []
    for k in k_list:
        ans.append(count.get(k, 0))
    return ' '.join(map(str, ans))

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    k_list = list(map(int, input().split()))
    print(pair_segments(n, arr, k_list))
