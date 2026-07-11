class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        count = {}

        for b in range(n - 3, 0, -1):

            # Add pairs (c, d) where c = b + 1 and d > c
            c = b + 1
            for d in range(c + 1, n):
                diff = nums[d] - nums[c]
                count[diff] = count.get(diff, 0) + 1

            # Count pairs (a, b)
            for a in range(b):
                ans += count.get(nums[a] + nums[b], 0)

        return ans