# mono stack problem
# For circular arrays, multiply it by 2.
# Time complexity: O(n)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums: return []
        #original length
        L1=len(nums)
        #double the nums
        nums+=nums
        L=len(nums)
        res=[-1 for _ in range(L)]
        stack=[]
        for i in range(len(nums)):
            while stack and nums[stack[-1]]<nums[i]:
                res[stack.pop()]=nums[i]
            stack.append(i)
        return res[:L1]
