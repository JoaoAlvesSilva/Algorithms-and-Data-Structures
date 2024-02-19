// https://leetcode.com/problems/sort-an-array

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        m = (len(nums)-1)//2 #middle index

        l = Solution().sortArray(nums[:(m+1)])
        r = Solution().sortArray(nums[(m+1):])

        return Solution().merge(l, r)

    def merge(self, l, r):
        # assume lists are sorted

        to_return = []

        i = 0
        j = 0

        while i < len(l) or j < len(r):

            if i >= len(l):
                to_return.append(r[j])
                j +=1
            elif j >= len(r):
                to_return.append(l[i])
                i +=1

            elif l[i] <= r[j]:
                to_return.append(l[i])
                i += 1
            else:
                to_return.append(r[j])
                j +=1
        return to_return
                   
        