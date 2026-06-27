class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:    
        i=0
        j=0
        ans=""
        l=max(len(word1),len(word2))
        while l>=0:
            if i<len(word1):
                ans+=word1[i]
                i+=1
            if j<len(word2):
                ans+=word2[j]
                j+=1
            l-=1
        return ans