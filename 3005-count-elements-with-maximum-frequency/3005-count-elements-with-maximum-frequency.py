class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        mx = max(freq.values())

        ans = 0
        for v in freq.values():
            if v == mx:
                ans += v

        return ans