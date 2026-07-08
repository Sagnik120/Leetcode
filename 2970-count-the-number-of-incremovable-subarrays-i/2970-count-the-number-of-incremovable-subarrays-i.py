class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        if i == n - 1:
            return n * (n + 1) // 2

        j = n - 1
        while j > 0 and nums[j - 1] < nums[j]:
            j -= 1

        ans = n - j + 1

        left = 0
        right = j

        while left <= i:
            while right < n and nums[left] >= nums[right]:
                right += 1

            ans += n - right + 1
            left += 1

        return ans