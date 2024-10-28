class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        a = {}
        l = {}
        r = {}
        for i,j in enumerate(nums):
            if j not in a:
                a[j] = 1
                l[j] = i 
            else:
                a[j] += 1
            r[j] = i 
        max_freq = max(a.values())
        ans = len(nums)
        for j in a:
            if a[j] == max_freq:
                ans = min(ans, r[j] - l[j] + 1)
        return ans