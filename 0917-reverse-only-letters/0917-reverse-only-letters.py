class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left=0
        right=len(s)-1
        s=list(s)
        while right>=left:
            if s[left].isalpha()==False:
                left+=1
            elif s[right].isalpha()==False:
                right-=1
            else:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
        return "".join(s)
