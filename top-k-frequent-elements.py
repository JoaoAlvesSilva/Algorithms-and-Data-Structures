// https://leetcode.com/problems/top-k-frequent-elements

import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = collections.defaultdict(list)

        for num in nums:
            if ans[num]==[]:
                ans[num] = 1
            else:
                ans[num]+=1

        target = collections.defaultdict(list)
        for key, value in list(ans.items()):
            target[value].append(key)

        tosort=list(ans.values())
        tosort.sort()

        tosort = list(dict.fromkeys(tosort))

        toreturn=[]

        i=-1
        while len(toreturn)< k:
            toreturn+= target[tosort[i]]
            i+=-1

        return toreturn
        


        