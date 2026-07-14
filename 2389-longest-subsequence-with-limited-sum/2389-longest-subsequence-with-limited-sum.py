class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        # Prefix sums
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        ans = []

        for q in queries:
            ans.append(bisect_right(nums, q))

        return ans

        