# tree traversal from parent to children+stack.
# build a hash table to map parent--->children
# Be careful that the leave nodes won't be added as keys into hash table in this question. Thus we need to add a if-sentence when pushign elements into the stack. 
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        Dict={}
        for i in range(len(ppid)):
            Dict.setdefault(ppid[i],[])
            Dict[ppid[i]].append(pid[i])
        stack=[]
        stack.append(kill)
        res=[]
        while stack:
            cur_kill=stack.pop()
            res.append(cur_kill)
            if cur_kill in Dict:
                for i in Dict[cur_kill]:
                    stack.append(i)
        return res
