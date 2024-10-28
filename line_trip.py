
def trip(arr, xx):
    if len(arr) == 0:
        return xx
    
    a = []
    a.append(arr[0])
    
    for i in range(1, len(arr)):
        y = arr[i] - arr[i - 1]
        a.append(y)
    
    a.append(2*(xx - arr[-1]))
    
    return max(a)

t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    
    if n > 0:
        stations = list(map(int, input().split()))
    else:
        stations = []
    
    print(trip(stations, x))
