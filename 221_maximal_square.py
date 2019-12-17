# DP, time complexity: O(mn)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        m=len(matrix)
        n=len(matrix[0])
        Dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
        max_edge=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    Dp[i+1][j+1]=1+min(Dp[i][j],Dp[i][j+1],Dp[i+1][j])
                    max_edge=max(max_edge, Dp[i+1][j+1])
        return max_edge*max_edge
