class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        l, h = 0, n

        while l <= h:
            x = (l + h) // 2

            # Find first index where nums[i] >= x
            left, right = 0, n - 1
            idx = n

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] >= x:
                    idx = mid
                    right = mid - 1
                else:
                    left = mid + 1

            count = n - idx

            if count == x:
                return x
            elif count > x:
                l = x + 1
            else:
                h = x - 1

        return -1