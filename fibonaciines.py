def max_fibonacciness(a1, a2, a4, a5):
    a = [a1 + a2, a4 - a2]  
    max_count = 0
    for a3 in a:
        count = 0
        if a3 == a1 + a2:
            count += 1
        if a4 == a2 + a3:
            count += 1
        if a5 == a3 + a4:
            count += 1
        max_count = max(max_count, count)
    return max_count
t = int(input())
for _ in range(t):
    a1, a2, a4, a5 = map(int, input().split())
    print(max_fibonacciness(a1, a2, a4, a5))

