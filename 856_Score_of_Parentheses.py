# stack problem
# when i==(: push into stack
# when i==): case 1: if peak element is (, then pop ( and push 1 into the stack
#           case 2: if peak element is a number, then create a temp var to sum all numbers until the peak element is (. then push 2*temp into stack
# an example to case2 is (()()())--------> (1,1,1)--->2*3=6

# after scanning, return the sum of the stack
# the trick for this problem is to store current val into stack
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack=[]
        for i in S:
            if i=='(':
                stack.append(i)
            else:
                if stack[-1]=='(':
                    stack.pop()
                    stack.append(1)
                else:
                    temp=0
                    while stack and stack[-1]!='(':
                        temp+=stack.pop()
                    stack.pop()
                    stack.append(2*temp)
        return sum(stack)
