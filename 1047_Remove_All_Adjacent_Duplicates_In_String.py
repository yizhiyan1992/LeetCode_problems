# stack
class Solution:
    def removeDuplicates(self, S: str) -> str:
        letter=list(S)
        stack=[]
        for i in letter:
            if stack and stack[-1]==i:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
