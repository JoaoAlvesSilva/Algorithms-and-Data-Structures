// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s=""
        for s1 in s:
            if s1.isalnum():
                if s1.isupper():
                    s2=s1.lower()
                    new_s += s2
                else:
                    new_s += s1
        ind=0
        while ind<len(new_s)/2.0 :
            if new_s[ind] != new_s[-1-ind]:
                break
            ind += 1
        
        return ind>=len(new_s)/2.0

        