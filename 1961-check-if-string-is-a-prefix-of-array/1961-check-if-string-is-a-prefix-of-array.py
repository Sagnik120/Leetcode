class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i=0
        j=0
        while i<len(s) and j<len(words):
            k=0
            d=words[j]
            while k<len(words[j]) and i<len(s):
                if s[i]!=d[k]:
                    return False
                i+=1
                k+=1

                if i == len(s) and k != len(words[j]):
                    return False
            j+=1
        
        return i==len(s)
                