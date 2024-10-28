def ans(a,b):
    return b-a
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(ans(a,b))