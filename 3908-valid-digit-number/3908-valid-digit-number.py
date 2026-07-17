class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        s1=list(str(n))
        s2=str(x)
        if s1[0]==s2:
            return False
        return True if s2 in s1 else False