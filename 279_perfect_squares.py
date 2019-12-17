# approach1: DP
# Time complexity: O(N*sqrt(N))
class Solution:
    def numSquares(self, n: int) -> int:
        DP=[float('inf') for _ in range(n+1)]
        DP[0]=0
        for i in range(1,n+1):
            square=1
            while square*square<=i:
                DP[i]=min(DP[i],DP[i-square*square]+1)
                square+=1
        return DP[-1]

A=[]
