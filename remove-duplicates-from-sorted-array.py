// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_new = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                pass
            else:
                nums_new.append(nums[i])
        k = len(nums_new)
        k2 = len(nums) - k
        for i in range(k2):
            nums_new.append(True)
        
        for i in range(len(nums)):
            nums[i] = nums_new[i]

        return k
            
        