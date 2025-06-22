import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")
def brrbrr():
    
t=int(input())
for i in range(t):
    n=int(input())
    col=[]
    for j in range(n):
        a=list(map(int,input().split()))
        col.append(a)
        