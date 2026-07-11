class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        frq={}
        for word in words:
            for i in word:
                frq[i]=frq.get(i,0)+1
        
        for key in frq:
            if frq[key]%len(words)!=0:
                return False
        return True