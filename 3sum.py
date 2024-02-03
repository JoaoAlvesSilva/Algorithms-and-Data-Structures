// https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=set()
        nums2=nums
        nums2.sort()
        for i1 in range(len(nums2)-2):
            if nums[i1] >0: 
                break
            i3 = len(nums2)-1
            i2= i1 + 1
            while i2  < i3:
                if nums2[i1]+nums2[i2]+nums2[i3] > 0:
                    i3 -= 1
                elif nums2[i1]+nums2[i2]+nums2[i3] < 0:
                    i2 += 1
                else:
                    result.add((nums2[i1],nums2[i2],nums2[i3]))
                    i2 += 1
        result_list = list(result)
        for i in range(len(result_list)):
            result_list[i] = list(result_list[i])
        return result_list
        