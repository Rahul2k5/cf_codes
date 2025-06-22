import heapq

def D(n, m, l, hurs, ps):
    pq = []
    cp = 1
    count = 0
    i = 0
    j = 0
    boool = True

    while i < n:
        while j < m and hurs[i][0] > ps[j][0]:
            heapq.heappush(pq, -ps[j][1]) 
            j += 1
        req = hurs[i][1] - hurs[i][0] + 2
        while pq and cp < req:
            count += 1
            cp += -heapq.heappop(pq) 
        if cp < req:
            boool = False
            break
        i += 1

    if not boool:
        return -1
    else:
        return count

t = int(input())
for _ in range(t):
    n, m, l = map(int, input().split())
    hurs = [list(map(int, input().split())) for _ in range(n)]
    ps = [list(map(int, input().split())) for _ in range(m)]
    print(D(n, m, l, hurs, ps))
    