#game-theory(min-max) problem1
#Use recurssion. Since each person wants to maximize their own score, it can be paraphrased in this way:
# B wants to minimize A's score as A wants to maximize the score of himself.

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        DP=[[None for _ in range(len(nums))] for _ in range(len(nums))]
        def dp(i, j, turn):
            if i == j:
                return nums[i] * (1 if turn else -1)
            elif i > j:
                return 0
            if turn:
                if DP[i+1][j]!=None and DP[i][j-1]!=None:
                    return max(DP[i+1][j]+nums[i],DP[i][j-1]+nums[j])
                else:
                    ans=max(dp(i + 1, j, False) + nums[i],dp(i, j - 1, False) + nums[j])
                    DP[i+1][j]=dp(i + 1, j, False)
                    DP[i][j-1]=dp(i, j - 1, False)
                    return ans
            else:
                if DP[i+1][j]!=None and DP[i][j-1]!=None:
                    return min(DP[i+1][j]-nums[i],DP[i][j-1]-nums[j])
                else:
                    ans=min(dp(i + 1, j, True) - nums[i],dp(i, j - 1, True) - nums[j])
                    DP[i+1][j]=dp(i + 1, j, True)
                    DP[i][j-1]=dp(i, j - 1, True)
                return ans

        return dp(0, len(nums) - 1, True) >= 0
