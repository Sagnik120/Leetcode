class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x=0
        for n in s+t:
            x^=ord(n)
        return chr(x)