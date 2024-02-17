// https://leetcode.com/problems/house-robber

class Solution:

    robberies = {}

    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        if len(nums) >=3:
            if tuple(nums) in Solution().robberies:
                return Solution().robberies[tuple(nums)]
            else:
                Solution().robberies[tuple(nums)] = max(nums[0]+Solution().rob(nums[2:]), Solution().rob(nums[1:]))
                return max(nums[0]+Solution().rob(nums[2:]), Solution().rob(nums[1:]))
        