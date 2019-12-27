#backtracking
#Note that it needs to return lexicographical order, so we need to sort for the bracket.
class Solution:
    def expand(self, S: str) -> List[str]:
        if not S: return []
        res=[]
        S=list(S)
        Len=len(S)
        def processing_bracket(depth):
            bracket=[]
            while S[depth]!='}':
                if S[depth]!=',':
                    bracket.append(S[depth])
                depth+=1
            bracket.sort() #lexicographical order
            return bracket,depth


        def helper(cur_res,depth):
            if depth==Len:
                res.append(''.join(cur_res))
                return
            if S[depth]!='{':
                cur_res.append(S[depth])
                helper(cur_res,depth+1)
                cur_res.pop()
            else:
                bracket,depth=processing_bracket(depth+1)
                for char in bracket:
                    cur_res.append(char)
                    helper(cur_res,depth+1)
                    cur_res.pop()
            return
        helper([],0)
        return res
