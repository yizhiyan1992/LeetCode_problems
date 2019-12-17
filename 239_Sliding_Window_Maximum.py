# deque problem
# use the stack to save the index, maintaining the decreasing stack
# For everytime, check if the most left element is behind the tail of the window, if yes then pop this element.
# Time complexity: O(n)

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        stack=deque([])
        res=[None for _ in range(len(nums)-k+1)]
        res[0]=max(nums[:k])
        for i in range(k):
            while stack and nums[stack[-1]]<nums[i]:
                stack.pop()
            stack.append(i)
        for i in range(k,len(nums)):
            while stack and nums[stack[-1]]<nums[i]:
                stack.pop()
            stack.append(i)
            while stack[0]<i-k+1:
                stack.popleft()
            res[i-k+1]=nums[stack[0]]
        return res
