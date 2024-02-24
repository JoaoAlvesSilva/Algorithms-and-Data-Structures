// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum = nums[0]
        Lm, Rm = 0, 0 #pointer for max sum
        currSum = 0
        L = 0 #pointer for current sum

        for R in nums:
            currSum += R

            if currSum > maxSum:
                maxSum = currSum
                Lm = L
                Rm = R

            if currSum <= 0:
                currSum = 0
                L = R
        return maxSum
                   
        