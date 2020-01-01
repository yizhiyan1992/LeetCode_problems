class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.lower()
        puncs=['!','?','\'',',',';','.']
        for punc in puncs:
            paragraph=paragraph.replace(punc,' ')
        paragraph_new=paragraph.split(' ')
        Dict={}
        for i in paragraph_new:
            if i not in banned and i!='':
                Dict.setdefault(i,0)
                Dict[i]+=1

        res_val=0
        res_key=None
        for key,value in Dict.items():
            if value>res_val:
                res_key=key
                res_val=value
        return res_key
