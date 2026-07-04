class Solution:
    def reverseVowels(self, s: str) -> str:
        left=0
        right=len(s)-1
        m=['a','e','i','o','u','A','E','I','O','U']
        s=list(s)
        while right>=left:
            if s[left] not in  m:
                left+=1
            elif s[right] not in m:
                right-=1
            else:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
        return "".join(s)