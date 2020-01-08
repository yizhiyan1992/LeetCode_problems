class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def recursion(substr,temp):
            if len(temp)==4 and substr=='':
                res.append(temp.copy())
                return
            if len(temp)>4 or substr=='': return
            temp.append(substr[-1])
            recursion(substr[:-1],temp)
            temp.pop()
            if len(substr)>1 and substr[-2]!='0':
                temp.append(substr[-2:])
                recursion(substr[:-2],temp)
                temp.pop()
            if len(substr)>2 and int(substr[-3:])<=255 and substr[-3]!='0':
                temp.append(substr[-3:])
                recursion(substr[:-3],temp)
                temp.pop()
            return
        res=[]
        recursion(s,[])
        for index,IP in enumerate(res):
            res[index]='.'.join(list(reversed(IP)))
        return res                
