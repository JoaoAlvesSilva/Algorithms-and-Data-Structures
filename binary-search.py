// https://leetcode.com/problems/binary-search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums)-1
        l = 0
        if target == nums[r]:
            return r
        if target == nums[l]:
            return l
        while r-l > 1:
            if target > nums[l+int((r-l)/2)]:
                l= l+int((r-l)/2)
            elif target < nums[l+ int((r-l)/2)]:
                r= l + int((r-l)/2)
            else:
                return l+int((r-l)/2)
        return -1

        