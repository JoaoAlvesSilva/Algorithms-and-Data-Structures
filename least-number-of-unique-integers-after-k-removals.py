// https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        l = {}

        for val in arr:
            if val in l:
                l[val] += 1
            else:
                l[val] = 1
        
        l1 = []
        for l2 in l.values():
            l1.append(l2)
        
        l1.sort()

        count = 0
        i = 0
        while count != k:
            l1[i] -= 1
            count +=1
            if l1[i] == 0:
                i += 1
        return (len(l1) - i)

        