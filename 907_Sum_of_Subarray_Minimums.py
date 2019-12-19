class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        left=[1 for _ in range(len(A))]
        right=[1 for _ in range(len(A))]

        stack=[]
        for i in range(len(A)):
            while stack and A[stack[-1]]>A[i]:
                index=stack.pop()
                left[i]+=left[index]
            stack.append(i)

        stack=[]
        for i in reversed(range(len(A))):
            while stack and A[stack[-1]]>=A[i]:
                index=stack.pop()
                right[i]+=right[index]
            stack.append(i)

        res=0
        for i in range(len(A)):
            res=res+A[i]*left[i]*right[i]
        return res%(10**9+7)
