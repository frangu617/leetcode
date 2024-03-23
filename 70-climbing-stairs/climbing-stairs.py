class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        prev1 = 1  # Number of ways to reach step 1
        prev2 = 2  # Number of ways to reach step 2
        
        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev1, prev2 = prev2, current
        
        return prev2
