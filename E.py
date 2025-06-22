def solve():
    t = int(input())
    results = []

    for _ in range(t):
        n = int(input())

        if n <= 4:
            results.append("-1")
        else:
            odd = list(range(1, n + 1, 2))
            even = list(range(2, n + 1, 2))

            if 5 in odd:
                odd.remove(5)
                odd.append(5)

            if 4 in even:
                even.remove(4)
                even.insert(0, 4)

            result = odd + even
            results.append(' '.join(map(str, result)))

    print('\n'.join(results))

solve()
