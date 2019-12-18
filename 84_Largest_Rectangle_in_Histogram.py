#mono stack, O(n)
# the explanation refers to https://www.cnblogs.com/boring09/p/4231906.html
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0
        Min_h=min(heights)
        heights.append(0)
        stack=[]
        Max_area=0
        for i in range(len(heights)):
            merge=0;peak=len(stack)-1
            while stack and peak>=0 and heights[stack[peak]]>heights[i]:
                # instead of popping up the elements from the stack, modyfying the heights that need to be popped, so that the stack can be non-decreasing.
                index=stack[peak]
                Max_area=max(Max_area,(i-index)*heights[index])
                heights[index]=heights[i]
                peak-=1
            stack.append(i)
        return Max_area
