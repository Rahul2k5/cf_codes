
def cover(n, cell):
    count=0
    count_dot=0
    max_dots=0
    for i in cell:
        if i==".":
            count_dot+=1
    for i in range(1,len(cell)-1):
        if cell[i-1]==cell[i]==cell[i+1]==".":
            count+=1
        else:
            count=max(max_dots,count)
    if count>=1:
        return 2
    else:
        return count_dot
        

t = int(input())
for i in range(t):
    n = int(input())
    cell = input().strip()
    print(cover(n, cell))
