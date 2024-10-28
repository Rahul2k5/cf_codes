def calculate_operations(n, lst):
    ans = float('inf')
    for j in range(1, n):
        ans = min(lst[j] - lst[j - 1], ans)
    ans = (ans + 2) // 2
    return max(0, ans)

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(calculate_operations(n, arr))