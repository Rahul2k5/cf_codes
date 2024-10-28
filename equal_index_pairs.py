import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

n = int(input())
index = [[] for _ in range(5001)]

arr = list(map(int, input().split()))

for i in range(0, 2 * n):
    index[arr[i]].append(i)

possible = True

for i in range(1, 5001):
    if len(index[i]) % 2 == 1:
        possible = False
        break

if possible:
    for i in range(1, 5001):
        for j in range(0, len(index[i]), 2):
            print(index[i][j] + 1, index[i][j + 1] + 1)
else:
    print("-1")
