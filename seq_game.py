def game(arr):
    ans = [arr[0]]
    for i in range(1, n):
        if arr[i] >= ans[-1]:
            ans.append(arr[i])
        else:
            ans.append(1)
            ans.append(arr[i])
    print(len(ans))
    return " ".join(map(str, ans))
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(game(arr))
    