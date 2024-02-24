// https://leetcode.com/problems/longest-turbulent-subarray

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        Lm, Rm = 0, 0 #pointers for max turbulent subarray

        L = 0

        next_bigger = True
        next_smaller = True

        for R in range(1,len(arr)):
            if R == L+1:
                if arr[R] > arr[L]:
                    next_bigger = False
                elif arr[R] < arr[L]:
                    next_smaller = False
                else: #arr[R] == arr[L]
                    L = R
            else:
                if next_bigger and arr[R] < arr[R-1]:
                    L = R - 1
                    next_bigger = True
                    next_smaller = False
                elif next_smaller and arr[R] > arr[R-1]:
                    L = R - 1
                    next_bigger = False
                    next_smaller = True
                elif arr[R] == arr[R-1]:
                    L = R
                    next_bigger= True
                    next_smaller = True
                else:
                    next_bigger = not(next_bigger)
                    next_smaller = not(next_smaller)
                
            if R - L > Rm - Lm:
                Lm, Rm = L, R


        return Rm-Lm+1
                   
        