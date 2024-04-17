// https://leetcode.com/problems/break-a-palindrome/

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        if len(palindrome) == 1:
            return ""
        # len(palindrome) is not 1

        s1 = ''

        i = 0
        while i < len(palindrome)//2:
            if palindrome[i] != 'a':
                s1 += 'a'
                s1 += palindrome[(i+1):]
                return s1
            else:
                s1 += 'a'
                i +=1
        s1 += palindrome[(len(palindrome)//2):(-1)]
        s1 += 'b'
        return s1

        