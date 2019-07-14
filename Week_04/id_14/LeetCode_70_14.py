class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        a1 = 1
        a2 = 2
        a3 = 0
        while(n > 2):
            a3 = a1 + a2
            a1 = a2
            a2 = a3
            a3 = 0
            n -= 1
        return a2
