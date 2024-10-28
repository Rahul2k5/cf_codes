def turtle_piggy_game(arr):
    arr.sort()
    return arr[len(arr)//2]
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(turtle_piggy_game(arr))
