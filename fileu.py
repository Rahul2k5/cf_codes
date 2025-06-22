""" find the sum of the elements in the array
    array =[1,2,[3,4],[5,[6,7]],8]"""
"""arr=[1,2,[3,4],[5,[6,7]],8]"""
arr=[]
def find_sum(arr):
    a=[]
    for i in arr:
        if isinstance(i,list):
            a.extend(find_sum(i))
        else:
            a.append(i)
    return a
ans=find_sum(arr)
tot_sum=sum(ans)
print(tot_sum)

