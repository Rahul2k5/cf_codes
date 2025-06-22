import sys
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")
def helmets(n,p,arr1,arr2):
    arr1.sort()
    arr2.sort()
    add=[]
    add_f=[]
    for i in range(n):
        if arr1[i]<p:
            add.append(arr1[i])
            add_f.append(arr2[i])
    ans=p
    for i in range(len(add)):
        ans+=add_f[i]*add[i]
    if sum(add_f)+1<n:
        ans+=p*(n-len(add_f))
    return ans

t=int(input())
for i in range(t):
    n,p=map(int,input().split())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    print(helmets(n,p,arr1,arr2))
    
