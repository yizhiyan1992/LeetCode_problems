#speed only beats 34%, slow
# Note: don't forget to create an inital case, where coin_0=0
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0: return 0
        coins.sort()
        Min_coins=[float('inf') for _ in range(amount+1)]
        Min_coins[0]=0
        for i in range(1,amount+1):
            for coin in coins:

                if i==coin:
                    Min_coins[i]=1
                elif i>coin:
                    Min_coins[i]=min(Min_coins[i],1+Min_coins[i-coin])
        return Min_coins[amount] if Min_coins[amount]!=float('inf') else -1
