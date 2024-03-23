class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize an array to store the number of distinct ways to reach each step
        dp = [0] * (n + 1)
        dp[1] = 1  # There's 1 way to climb to step 1
        dp[2] = 2  # There are 2 ways to climb to step 2 (1 step + 1 step or 2 steps)
        
        # Calculate the number of distinct ways to climb to each step
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]  # Number of ways to reach step i is sum of ways to reach step (i-1) and (i-2)
        
        return dp[n]  # Return the number of distinct ways to climb to the top