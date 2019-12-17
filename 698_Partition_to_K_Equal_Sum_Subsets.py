# backtracking problem
# use a boolean array to mark all visited nodes
# sum all value, if it cannot be partitioned into k subsets, return False

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # sum all value, if it cannot be partitioned into k subsets, return False
        if sum(nums)%k!=0: return False
        n=len(nums)
        target=int(sum(nums)/k)
        visit=[False for _ in range(n)]
        def backtrack(array,start,currentSum,k,ans):
            # when k=1, it must succeed!
            if k==1: return True
            # when currensum is larger than target, it means impossible for current combination, just return
            if currentSum>target:
                return
            if start>=n: return
            # when found one combination that meet the requirement, go to next recursion with k-1 subsets. Reset start point
            if currentSum==target:
                ans=backtrack(array,0,0,k-1,ans)
                if ans:
                    return True
            for i in range(start,n):
                if visit[i]==False:
                    currentSum=currentSum+nums[i]
                    visit[i]=True
                    ans=backtrack(array,i+1,currentSum,k,ans)
                    if ans: return True
                    visit[i]=False
                    currentSum=currentSum-nums[i]
            return ans
        ans=backtrack(nums,0,0,k,False)
        return ans
