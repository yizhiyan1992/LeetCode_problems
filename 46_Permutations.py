#backtracking
#To move the element in the array and put it back at original postion take O(n) time.
#Because all elements are distinct, we can use a set to do the backtracking!
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        res=[]
        record=set()
        def helper(nums,cur_res):
            if len(record)==len(nums):
                res.append(cur_res.copy())
                return
            for i in nums:
                if i not in record:
                    record.add(i)
                    cur_res.append(i)
                    helper(nums,cur_res)
                    cur_res.pop()
                    record.remove(i)
            return
        helper(nums,[])
        return res
