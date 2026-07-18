class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights[:]
        m = max(expected)
        count = [0] * (m+1)
        for i in expected:
            count[i] += 1
        j = 0
        for i in range(len(count)):
            while count[i] > 0:
                expected[j] = i
                j += 1
                count[i] -= 1
        count = 0
        for i,j in zip(heights,expected):
            if i != j:
                count += 1
        return count