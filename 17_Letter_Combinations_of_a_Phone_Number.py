#backtracking problem
#two things need to be backtracked 1) the cur_res 2) the sequence of the digits.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        Phone={2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
        digits=list(digits)
        digits.reverse()
        res=[]
        def helper(digits,cur_res):
            if not digits:
                res.append(''.join(cur_res))
                return
            cur_digit=int(digits.pop())
            for i in Phone[cur_digit]:
                cur_res.append(i)
                helper(digits,cur_res)
                cur_res.pop()
            digits.append(cur_digit)
            return
        helper(digits,[])
        return res
