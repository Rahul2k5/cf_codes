def intercepted(arr):
    tar = k - 2
    fctor = []
    for i in range(1, int(tar**0.5) + 1):
        if tar % i == 0:
            fctor.append(i)
            if i != tar // i:
                fctor.append(tar // i)
    arr.sort()
    boool = False
    for n in fctor:
        m = tar // n
        if n in arr and m in arr:
            print(n, m)
            boool = True
            break
    if not boool:
        print(-1)

t = int(input())
for i in range(t):
    k = int(input())
    arr = list(map(int, input().split()))
    intercepted(arr)
