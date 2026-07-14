class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)

        ans = []
        curr = 0
        total = sum(nums)

        for num in nums:
            ans.append(num)
            curr += num

            if curr > total - curr:
                break

        return ans