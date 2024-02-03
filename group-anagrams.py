// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for word in strs:
            count = [0]*26
            for w in word:
                count[ord(w)-ord('a')] +=1
            ans[tuple(count)].append(word)
        return ans.values()
