class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)

        # Find first non-negative
        while i < n and nums[i] < 0:
            i += 1

        j = i - 1
        ans = []

        # Merge
        while j >= 0 and i < n:
            if abs(nums[j]) <= nums[i]:
                ans.append(nums[j] * nums[j])
                j -= 1
            else:
                ans.append(nums[i] * nums[i])
                i += 1

        # Remaining negatives
        while j >= 0:
            ans.append(nums[j] * nums[j])
            j -= 1

        # Remaining positives
        while i < n:
            ans.append(nums[i] * nums[i])
            i += 1

        return ans