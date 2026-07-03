class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)

        ans = high

        while low <= high:

            mid = (low + high) // 2

            pieces = 1
            current = 0

            for num in nums:

                if current + num <= mid:
                    current += num

                else:
                    pieces += 1
                    current = num

            if pieces <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans