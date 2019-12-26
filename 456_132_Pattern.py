#use mono stack
# reverse the nums array, and maintain a decresing stack.
#In this case, the peak element of the stack can be regarded as 3 in 1-3-2
# 2 in 1-3-2 is the max value that were popped out from the stack (now, all elements in stack are larger than 2)
# and 1 is the current element is nums. If 1 is smaller than 2, return True.
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        nums.reverse()
        stack=[]
        V2=-float('inf')
        for i in nums:
            if i<V2:
                return True
            while stack and stack[-1]<i:
                temp=stack.pop()
                V2=max(V2,temp)
            stack.append(i)
        return False
