def calculate_points_from_grid(a, b, c, d, e, f, g, h, i ,j):
    ans = 0
    rows=[a,b,c,d,e,f,g,h,i,j]
    n = len(rows) 
    m = len(a)  

    for i in range(n * m):
        row = i // m
        col = i % m
        
        if rows[row][col]=='X':
            ring = min(row, n - 1 - row, col, m - 1 - col)
            ans += ring + 1
    
    return ans

t=int(input())
for i in range(t):
    a=input()
    b=input()
    c=input()
    d=input()
    e=input()
    f=input()
    g=input()
    h=input()
    i=input()
    j=input()
    print(calculate_points_from_grid(a, b, c, d, e, f, g, h, i ,j))
