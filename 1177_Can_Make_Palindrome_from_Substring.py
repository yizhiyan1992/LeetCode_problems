'''
note 1: how to solve palidrome problem
note 2: how to index the number of letters given a substring s[i:j] by constant time?
---> create a prefix array [len(s),26], then we accumulate the number for each letter, and use row j - row i. O(1)
p.s use append method to create the prefix array is faster than create prefix array directly... (why?)
'''
def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
    def Query(bin1,bin2,k):
        single_count=0
        for i in range(26):
            single_count+=(bin2[i]-bin1[i])%2
        return single_count//2<=k

    res=[]
    bins=[[0 for _ in range(26)]]
    for i in range(len(s)):
        bins.append(bins[-1][:])
        bins[i+1][ord(s[i])-ord('a')]+=1
    for query in queries:
        res.append(Query(bins[query[0]],bins[query[1]+1],query[2]))
    return res
