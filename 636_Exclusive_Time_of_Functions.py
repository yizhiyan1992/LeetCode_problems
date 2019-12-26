#Stack
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack=[]
        res=[0 for _ in range(n)]
        last_time=0
        for i in logs:
            log=i.split(':')
            ID=int(log[0]);construct=log[1];timestamp=int(log[2])
            if stack and construct=='start':
                res[stack[-1]]+=timestamp-last_time
                stack.append(ID)
            elif stack and construct=='end':
                timestamp+=1
                last_ID=stack.pop()
                res[ID]+=timestamp-last_time
            else:
                stack.append(ID)
            last_time=timestamp
        return res
