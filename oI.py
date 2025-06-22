def game(s):
    count = 0
    i = 0
    while i < len(s) - 1:
        if s[i:i+2] == "10" or s[i:i+2] == "01":
            s = s[:i] + s[i+2:]
            count += 1
            i = max(i - 1, 0)
        else:
            i += 1
    if count % 2 == 0:
        return "NET"
    return "DA"
t = int(input())
for _ in range(t):
    s = input()
    print(game(s))
