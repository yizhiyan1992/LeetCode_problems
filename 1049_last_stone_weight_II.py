# Medium.
# Dynamic programming, time complexity: O(N*M)  space complexity: O(M)
# key idea: the stones can be divided into two set (you can imagine heat one stone in the set with one stone in another set,
# and the final value will be the different of the sums of the two sets)
# following this idea, it can be transformed into subset sum problem/
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        if not stones: return 0
        capacity=sum(stones)
        DP=[False for _ in range(capacity+1)]
        DP[0]=True
        for i in stones:
            temp=DP.copy()
            for j in range(len(DP)):
                if DP[j]==True:
                    temp[j+i]=True
            DP=temp
        ans=float('inf')
        for i in range(len(DP)):
            if DP[i]==True:
                pack1=i;pack2=capacity-i
                ans=min(ans,abs(pack1-pack2))
        return ans
