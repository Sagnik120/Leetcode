class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        ans = 1
        while '0' in str(ans) or '0' in str(n - ans):
            ans += 1
            
        return [ans, n - ans]