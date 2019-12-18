# Stack problem, easy, time complexity: O(n)
# Three cases to output False
# 1) mismatch '[' with '}'
# 2) remaining brackets in stack ['{', '(', '(']
# 3) When encounter a close bracket, the stack is empty. (important!)
class Solution:
    def isValid(self, s: str) -> bool:
        parentheses=list(s)
        stack=[]
        for i in parentheses:
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            elif i==')':
                if not stack or stack.pop()!='(':
                    return False
            elif i=='}':
                if not stack or stack.pop()!='{':
                    return False
            elif i==']':
                if not stack or stack.pop()!='[':
                    return False
        if stack:
            return False
        return True
