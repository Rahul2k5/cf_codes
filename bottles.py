import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

n = int(input())
a = []
b = []
for i in range(n):
    a1, b1 = map(int, input().split())
    a.append(a1)
    b.append(b1)

def bottles(n, a, b):
    openable_brands = set()
    
    for i in range(n):
        if a[i] != b[i]:
            openable_brands.add(b[i])
    
    unopenable_count = sum(1 for i in range(n) if a[i] not in openable_brands)

    return unopenable_count

print(bottles(n, a, b))
