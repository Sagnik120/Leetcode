class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s=str(n)
        ans=0
        p=1
        for ch in range(len(s)):
            ans+=int(s[ch])*p
            p*=-1
        return ans
