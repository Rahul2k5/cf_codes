def fix(sers):
    x = int(s[0])
    y = s[1]
    z = int(s[2])
    if (y == '<' and x < z) or (y == '>' and x > z) or (y == '=' and x == z):
        return s
    if x < z:
        return f"{x}<" + str(z)
    elif x > z:
        return f"{x}>" + str(z)
    else: 
        return f"{x}=" + str(z)
t = int(input())  
for i in range(t):
    s=input()
    print(fix(s))
