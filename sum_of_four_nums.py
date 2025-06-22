class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        a = {}
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                x = nums[i] + nums[j]
                if x not in a:
                    a[x] = []
                a[x].append([i, j])
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                y = target - nums[i] - nums[j]
                if y in a:
                    for k in a[y]:
                        if k[0] != i and k[1] != j:
                            ans.add(tuple(sorted([nums[k[0]], nums[k[1]], nums[i], nums[j]])))
        return [list(quadruple) for quadruple in ans]
