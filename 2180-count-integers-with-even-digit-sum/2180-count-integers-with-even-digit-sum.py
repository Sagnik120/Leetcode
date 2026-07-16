class Solution:
    def countEven(self, num: int) -> int:
        ans=0
        def helper(n):
            s = str(n)
            a = 0
            for char in s:
                a += int(char)
            return a % 2 == 0
        
        for i in range(1, num + 1):
            ans += helper(i)
        return ans