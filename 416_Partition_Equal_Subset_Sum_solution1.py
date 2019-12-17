#solution 1: DP
# Sum all values
# Case 1: if the sum is an odd number, then it is impossible to divide into two subsets
# Case 2: if the sum is an even number, then visit the DP array [sum/2] to see if this cell is True/False (This is because DP[sum/2] can witness whether one combination of subarray can sum to this value)
# Dp[i][j]: whether we can sum to j using first i numbers
# Dp[i][j]=True if Dp[i][j+num_i]
# Check Dp[n-1][Sum/2]
# init dp[-1][0]=true (Note that the lrngth of Dp array should be sum+1!!!)
# Time complexity: O(n*sum)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        Sum=sum(nums)
        if Sum%2==1:
            return False
        DP=[False for _ in range(Sum+1)]
        DP[0]=True
        for i in nums:
            temp=DP.copy()
            for j in range(len(DP)):
                if DP[j]==True:
                    temp[j+i]=True
            DP=temp
        return DP[int(Sum/2)]
