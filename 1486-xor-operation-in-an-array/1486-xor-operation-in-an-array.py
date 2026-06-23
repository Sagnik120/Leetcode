class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans=0
        while n!=0:
            ans^=start
            start+=2
            n-=1
        return ans