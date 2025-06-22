t = int(input())
for i in range(t):
    a, b, c, d = map(int, input().split())
    if a == b and a == c and a == d:
        print("Yes")
    else:
        print("No")