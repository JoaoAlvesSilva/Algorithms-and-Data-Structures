// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        no_sol = True
        ind1 = 0
        ind2 = 1
        while no_sol == True:
            no_sol= not nums[ind1]+nums[ind2]==target
            if no_sol==True:
                ind2 += 1
                if ind2 == len(nums):
                    ind1 += 1
                    ind2 = ind1+1
        return [ind1, ind2]
                   
        