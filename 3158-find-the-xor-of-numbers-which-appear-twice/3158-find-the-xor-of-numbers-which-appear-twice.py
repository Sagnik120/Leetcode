class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        xor_nums = 0
        xor_set = 0

        for num in nums:
            xor_nums ^= num

        for num in set(nums):
            xor_set ^= num

        return xor_nums ^ xor_set