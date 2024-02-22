// https://leetcode.com/problems/kth-largest-element-in-a-stream


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.num = k
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.num]

                   
        