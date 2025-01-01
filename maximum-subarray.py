// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_end_here= -float("inf")
        max_so_far= -float("inf")
        for num in nums:
            max_end_here = max(num, max_end_here + num)
            max_so_far = max(max_end_here, max_so_far)
        return max_so_far
                   
        