// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        open_brkc = ['(','{','[']
        closed_brkc = [')','}',']']
        queue=[]
        for c in s:
            if c in open_brkc:
                queue.append(c)
            if c in closed_brkc:
                ind= closed_brkc.index(c)
                if queue !=[] and open_brkc[ind]==queue[-1]:
                    queue.pop(-1)
                else:
                    return False
        return queue==[]
                   
        