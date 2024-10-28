import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

def bright(n):
    a=[0]

t = int(input())
for _ in range(t):
    n = int(input())
    print(bright(n))
