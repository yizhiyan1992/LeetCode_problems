# PD problem
# Be careful when setting the initial DP array. This problem is a minimization problem.
# the initial DP array looks like:
#   inf 0 inf ... inf
#       _____________
#   0  |  inf ... inf
#   inf|  inf ... inf
#   inf|  inf ... inf
# DP[0][1] and DP[1][0] should be 0, otherwise the answer will be inf!
# It is recommended to come up with a toy example and write down on manuscript first!
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m=len(grid)
        n=len(grid[0])
        DP=[[float('inf') for _ in range(n+1)] for _ in range(m+1)]
        DP[0][1]=0;DP[1][0]=0 #this step is very important!
        for i in range(m):
            for j in range(n):
                DP[i+1][j+1]=grid[i][j]+min(DP[i][j+1],DP[i+1][j])
        return DP[-1][-1]
