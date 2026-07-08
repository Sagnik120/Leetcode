class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        ans = 0

        while left <= right:
            if left == right:
                ans += nums[left]
            else:
                ans += int(str(nums[left]) + str(nums[right]))

            left += 1
            right -= 1

        return ans

        