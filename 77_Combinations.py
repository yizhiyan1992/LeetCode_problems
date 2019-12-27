#backtracking
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k==0: return []
        nums=list(range(1,n+1))
        res=[]
        def helper(cur_res,depth):
            if len(cur_res)==k:
                res.append(cur_res.copy())
                return
            for i in range(depth,n):
                cur_res.append(nums[i])
                helper(cur_res,i+1)
                cur_res.pop()
            return
        helper([],0)
        return res
