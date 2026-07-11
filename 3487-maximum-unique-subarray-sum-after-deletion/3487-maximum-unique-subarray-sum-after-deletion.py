class Solution:
    def maxSum(self, nums: List[int]) -> int:
        mx = max(nums)

        if mx <= 0:
            return mx

        seen = set()
        ans = 0

        for num in nums:
            if num > 0 and num not in seen:
                ans += num
                seen.add(num)

        return ans