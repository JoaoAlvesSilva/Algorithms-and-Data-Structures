// https://leetcode.com/problems/unique-paths

class Solution:

    cache = {}

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1:
            return 1
        if n == 1:
            return 1
        if (m, n) in Solution().cache:
            return Solution().cache[(m, n)]

        Solution().cache[(m, n)] =  Solution().uniquePaths(m-1, n) + Solution().uniquePaths(m, n - 1)
        return Solution().cache[(m, n)]
        