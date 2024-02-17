// https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []
        elif len(nums) == 1:
            return [ [], [nums[0]]]
        else:
            list1 = Solution().subsets(nums[1:])
            list2 = [[nums[0]] + l1 for l1 in list1]
            return list1+list2


        