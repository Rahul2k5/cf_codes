
def game(x):
    if (x-1)%3==0 or (x+1)%3==0:
        return "First"
    return "Second"

t = int(input())
for i in range(t):
    y = int(input())
    print(game(y))