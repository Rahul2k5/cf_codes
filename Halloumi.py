def can_sort_boxes(n, k, boxes):
    if k >= n:
        return "YES"
    
    if k == 1:
        return "YES" if boxes == sorted(boxes) else "NO"
    
    return "YES"
t=int(input())
for i in range(t):
    n, k = map(int, input().split())
    boxes = list(map(int, input().split()))
    print(can_sort_boxes(n, k, boxes))
