def fav_perm(n):
    if n <= 4:
        return "-1"
    else:
        o,e = [], []
        for i in range(1, n + 1):
            if i % 2 == 1:
                o.append(i)
            else:
                e.append(i)
        if 5 in o:
            o.remove(5)
            o.append(5)
        if 4 in e:
            e.remove(4)
            e.insert(0, 4)
        result = o + e
        return " ".join(map(str, result))

t = int(input())
for i in range(t):
    n = int(input())
    print(fav_perm(n))
