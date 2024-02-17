// https://leetcode.com/problems/remove-element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_new = []
        for num in nums:
            if num != val:
                nums_new.append(num)
        k= len(nums_new)
        k2 = len(nums) - len(nums_new)
        for i in range(k2):
            nums_new.append(True)
        for i in range(len(nums)):
            nums[i] = nums_new[i]
        return k
            
        