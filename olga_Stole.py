
n = input().strip()
bag = list(map(int, input().split()))
total_sum=sum(bag)
count=0
for i in bag:
    x=total_sum-i
    if x%2==0:
        count+=1
print(count)
