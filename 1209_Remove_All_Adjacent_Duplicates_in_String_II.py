# stack, time complexity: O(n)
# To solve this problem, lets build 2 stacks (stack2 is an auxiliary stack)
# Stack2 is used to store the number of elements corresponding to stack 1 appeared already in previous continuous positions
# When the number in stack2 is equal to k, the element pops out from stack.
# Be careful that stack1 is not the final answer. For each element is stack1, it needs to expand by multiplying the corresponding number in stack2 to get the final answer.
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack1=[]
        stack2=[]
        for i in s:
            if not stack1:
                stack1.append(i)
                stack2.append(1)
            else:
                if stack1[-1]==i:
                    stack2[-1]+=1
                    if stack2[-1]>=k:
                        stack1.pop()
                        stack2.pop()
                else:
                    stack1.append(i)
                    stack2.append(1)
        ans=[i*j for i,j in zip(stack1,stack2)]
        return ''.join(ans)
