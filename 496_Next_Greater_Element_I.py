#monostack problem
#Keep the stack with decreasing order, when an element gonna be added in the stack, examine weather it is smaller than the peak element of the stack.
# If yes, then put the element in the stack. If no, then pop the peak element and put the answer in array[stack[peak]]. Then, repeat this process until the last element is tested.
# Note: the length of the asnwer array is max(nums1), instead of len(nums1)
#Time complexity: O(n)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1: return []
        Max=max(nums2)
        store=[-1 for _ in range(Max+1)]
        monostack=[float('inf')]
        i=0
        while i<=len(nums2)-1:
            if nums2[i]<monostack[-1]:
                monostack.append(nums2[i])
                i+=1
            else:
                value=monostack.pop()
                store[value]=nums2[i]
        ans=[]
        for i in nums1:
            ans.append(store[i])
        return ans
