// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i1 in range(len(numbers)):
            i2= len(numbers)-1
            while numbers[i1]+numbers[i2] >= target:
                if numbers[i1]+numbers[i2] == target:
                    return (i1+1, i2+1)
                else:
                    i2 += -1



        