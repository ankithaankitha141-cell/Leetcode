class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # Path length must be even
        if (m + n - 1) % 2 == 1:
            return False

        # dp[j] = possible balance values at current row, column j
        dp = [[set() for _ in range(n)] for _ in range(m)]

        if grid[0][0] == ')':
            return False

        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                for balance in range(m + n):
                    possible = False

                    if i > 0 and balance in dp[i - 1][j]:
                        possible = True

                    if j > 0 and balance in dp[i][j - 1]:
                        possible = True

                    if not possible:
                        continue

                    if grid[i][j] == '(':
                        new_balance = balance + 1
                    else:
                        new_balance = balance - 1

                    if new_balance >= 0:
                        dp[i][j].add(new_balance)

        return 0 in dp[m - 1][n - 1]