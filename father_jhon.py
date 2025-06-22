def jhon_father(a, n, m):
    a.sort()
    s = -1
    valid = True
    for i in range(m):
        for j in range(n):
            cards = a[j][0]
            if cards[i] > s:
                s = cards[i]
            else:
                valid = False
                break
        if not valid:
            break
    if valid:
        print(" ".join(str(cow[1]) for cow in a))
    else:
        print(-1)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        cards = list(map(int, input().split()))
        cards.sort()  
        a.append((cards, i + 1))  
    jhon_father(a, n, m) 
