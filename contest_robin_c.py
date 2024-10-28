def can_make_unhappy_more_than_half(n, arr, x):
    a = sum(arr)
    new_total_wealth = a + x
    half_average = new_total_wealth / (2 * n)
    count = 0
    for i in arr:
        if i < half_average:
            count += 1
    return count > n // 2

def better_call_robin(n, arr):
    a = sum(arr)
    count = 0
    for i in arr:
        if i < a / (2 * n):
            count += 1
    
    if count > n // 2:
        return 0
    
    if n <= 2:
        return -1
    
    arr.sort()  
    l, r = 0, 4 * 10**12  
    ans = -1
    while l <= r:
        m = l + (r - l) // 2
        if can_make_unhappy_more_than_half(n, arr, m):
            ans = m
            r = m - 1
        else:
            l = m + 1

    return ans if ans != -1 else -1

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(better_call_robin(n, arr))
