#Backtrcking
#set a counter to record how many '(' in current res, if the counter is 0, it must add '(', otherwise it can add either ( or ), and recur.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n: return ['']
        left=['(' for _ in range(n)]
        right=[')' for _ in range(n)]
        res=[]
        def helper(counter,cur_res):
            if not left and not right:
                res.append(''.join(cur_res))
                return
            if counter==0:
                cur_res.append(left.pop())
                helper(counter+1,cur_res)
                cur_res.pop()
                left.append('(')
            else:
                if left:
                    cur_res.append(left.pop())
                    helper(counter+1,cur_res)
                    cur_res.pop()
                    left.append('(')
                if right:
                    cur_res.append(right.pop())
                    helper(counter-1,cur_res)
                    cur_res.pop()
                    right.append(')')
            return
        helper(0,[])
        return res
