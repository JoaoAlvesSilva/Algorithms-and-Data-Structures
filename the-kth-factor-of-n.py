// https://leetcode.com/problems/the-kth-factor-of-n

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        listFactor=[i for i in range(1,n+1) if n % i==0]
        if len(listFactor) < k:
            return -1
        else:
            return listFactor[k-1]
        