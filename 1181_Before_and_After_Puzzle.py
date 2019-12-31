#string problem
class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        first={}
        res=[]
        for i in range(len(phrases)):
            word1=phrases[i].split(' ')
            end=word1[-1]
            for j in range(len(phrases)):
                #because the word cannot merge with itself
                if i!=j:
                    word2=phrases[j].split(' ')
                    start=word2[0]
                    if start==end:
                        res.append(' '.join(word1+word2[1:]))
        #there might be duplicates in the list
        res=list(set(res))
        #lexigraphically ordered
        res.sort()
        return res
