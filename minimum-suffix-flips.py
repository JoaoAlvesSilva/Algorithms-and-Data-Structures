// https://leetcode.com/problems/minimum-suffix-flips

class Solution:
    def minFlips(self, target: str) -> int:

        n = len(target)
        num = 0 

        for i in range(n):
            if target[i] == '1' and num % 2 ==0:
                num += 1
            if target[i] == '0' and num % 2 ==1:
                num += 1
        return num
        

        