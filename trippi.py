def trippi(s):
    a=s.split()
    ans=''
    for i in a:
        ans+=i[0]
    return ans
t=int(input())
for i in range(t):
    s=str(input())
    print(trippi(s))
