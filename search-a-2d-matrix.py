// https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #search through the rows
        l = 0
        r= len(matrix)-1

        if target < matrix[l][0]:
            return False
        if target > matrix[r][-1]:
            return False
        if target == matrix[l][ 0] or target == matrix[r][ 0]:
            return True
        
        if target > matrix[r][0]:
            l = r
        
        
        while l < r -1:
            m = l + (r-l)//2
            if target > matrix[m][ 0]:
                l = m 
            elif target < matrix[m][ 0]:
                r = m
            elif target == matrix[m][0]:
                return True
            

        #search through the columns

        l_c = 0
        r_c = len(matrix[l])-1


        if target == matrix[l][ l_c] or target == matrix[l][ r_c]:
            return True
        
        while l_c < r_c -1:
            m_c = l_c + (r_c-l_c)//2
            if target > matrix[l][ m_c]:
                l_c = m_c 
            elif target < matrix[l][ m_c]:
                r_c = m_c
            elif target == matrix[l][ m_c]:
                return True
        return False
        

        