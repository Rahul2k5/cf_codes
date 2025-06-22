def dr_tc(n,m):
    a=[]
    count=0
    for i in range(n):
        if m[i-1]=="0":
            a.append(m[:i]+"1"+m[i+1:])
        elif m[i-1]=="1":
            a.append(m[:i]+"0"+m[i+1:])
    for i in range(len(a)):
        for j in a[i]:
            if j=="1":
                count+=1
    return count
t=int(input())
for i in range(t):
    n=int(input())
    m=str(input())
    print(dr_tc(n,m))