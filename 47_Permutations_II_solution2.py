#solution 2 to remove duplicates.
#1) sort the order of nums first.
#2) for the same number, it can be used only if its prior same number are used.
# e.g. [1,1,1,3,4,4] for number 1, the third 1 can only be used if the first two 1s are used. Otherwise it cannot be used.
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        visit=[False for _ in range(len(nums))]
        nums.sort()
        res=[]

        def helper(cur_res,counter):
            if counter==0:
                res.append(cur_res.copy())
                return
            for i in range(len(nums)):
                if i==0:
                    if visit[0]==False:
                        visit[0]=True
                        cur_res.append(nums[i])
                        helper(cur_res,counter-1)
                        cur_res.pop()
                        visit[0]=False
                elif nums[i]!=nums[i-1]:
                    if visit[i]==False:
                        visit[i]=True
                        cur_res.append(nums[i])
                        helper(cur_res,counter-1)
                        cur_res.pop()
                        visit[i]=False
                elif nums[i]==nums[i-1]:
                    if visit[i-1]==True and visit[i]==False:
                        visit[i]=True
                        cur_res.append(nums[i])
                        helper(cur_res,counter-1)
                        cur_res.pop()
                        visit[i]=False
            return
        helper([],len(nums))
        return res
