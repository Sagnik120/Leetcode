class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        x = min(freq.keys())
        for y in sorted(freq.keys()):
            if y > x and freq[y] != freq[x]:
                return [x, y]
        return [-1, -1]