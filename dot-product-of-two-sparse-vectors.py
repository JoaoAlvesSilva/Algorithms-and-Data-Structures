// https://leetcode.com/problems/dot-product-of-two-sparse-vectors

class SparseVector:
    def __init__(self, nums: List[int]):
        self.vals = {i : nums[i] for i in range(len(nums)) if nums[i] != 0}

        #self.indx = [i for i in range(len(nums)) if nums[i] != 0]        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for ind in self.vals:
            if ind in vec.vals:
                result += self.vals[ind]*vec.vals[ind]
        return result
                   
        