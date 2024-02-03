// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_noduplicate=list(set(nums))
        nums.sort()
        nums_noduplicate.sort()
        return not nums==nums_noduplicate
