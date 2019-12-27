# backtracking
# How to remove duplicates?
# Solution one: record the number of every elements in Dict, and turn list into set. e.g. [1,2,1] will be [1,2]
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        Dict={}
        res={}
        counter=len(nums)
        for i in nums:
            Dict.setdefault(i,0)
            Dict[i]+=1
        nums=list(set(nums))
        def helper(counter,cur_res):
            if counter==0:
                res[str(cur_res)]=cur_res.copy()
                return
            for i in nums:
                if Dict[i]>0:
                    Dict[i]-=1
                    cur_res.append(i)
                    helper(counter-1,cur_res)
                    cur_res.pop()
                    Dict[i]+=1
            return
        helper(counter,[])
        return list(res.values())
