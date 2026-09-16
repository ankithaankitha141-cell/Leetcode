class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j] = number of ways to draw j segments using points up to index i
        dp = [[0] * (k + 1) for _ in range(n)]
        
        for i in range(n):
            dp[i][0] = 1  # Base case: 1 way to draw 0 segments
            
        for j in range(1, k + 1):
            prefix_sum = 0
            for i in range(1, n):
                prefix_sum = (prefix_sum + dp[i - 1][j - 1]) % MOD
                dp[i][j] = (dp[i - 1][j] + prefix_sum) % MOD
                
        return dp[n - 1][k]