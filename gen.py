def gen(n):
    if n%2==0:
        return "NO"
    return "YES"
t=int(input())
for i in range(t):
    n=int(input())
    print(gen(n))