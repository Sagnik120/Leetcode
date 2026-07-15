class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        # First index of >= 0
        l, h = 0, n - 1
        first_non_negative = n

        while l <= h:
            mid = l + (h - l) // 2

            if nums[mid] >= 0:
                first_non_negative = mid
                h = mid - 1
            else:
                l = mid + 1

        neg = first_non_negative

        # First index of > 0
        l, h = 0, n - 1
        first_positive = n

        while l <= h:
            mid = l + (h - l) // 2

            if nums[mid] > 0:
                first_positive = mid
                h = mid - 1
            else:
                l = mid + 1

        pos = n - first_positive

        return max(neg, pos)