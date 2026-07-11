class Solution:
    def maxSum(self, nums: List[int]) -> int:
        best = {}
        ans = -1

        for num in nums:
            mx = max(str(num))  # maximum digit as a character

            if mx in best:
                ans = max(ans, num + best[mx])
                best[mx] = max(best[mx], num)
            else:
                best[mx] = num

        return ans