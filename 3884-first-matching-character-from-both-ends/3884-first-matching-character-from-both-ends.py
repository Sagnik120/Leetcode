class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        l=0
        r=len(s)-1

        while r>=l:
            if s[l]==s[r]:
                return l
            l+=1
            r-=1

        return -1