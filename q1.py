"""
Given an array of integers sorted in ascending order and a target value, 
return the indexes of any pair of numbers in the array that sum to the target.
The order of the indexes in the result doesn't matter. If no pair is found, return an empty array.

Example 1:
Input: nums = [-5, -2, 3, 4, 6], target = 7
Output: [2, 3]
"""
import sys
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")

def two_sum(arr,target):
    ans=[]
    a={}
    for i in range(len(arr)):
        if target-arr[i] in a:
            ans.append([i,a[target-arr[i]]])
        a[arr[i]]=i
    return ans

t=int(input())
for i in range(t):
    target=int(input())
    arr=list(map(int,input().split()))
    print(two_sum(arr,target))

