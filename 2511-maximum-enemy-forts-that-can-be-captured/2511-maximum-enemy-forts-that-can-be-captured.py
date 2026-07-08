class Solution:
    def captureForts(self, forts: List[int]) -> int:
        prev = -1
        ans = 0

        for i in range(len(forts)):
            if forts[i] != 0:
                if prev != -1 and forts[i] != forts[prev]:
                    ans = max(ans, i - prev - 1)
                prev = i

        return ans