class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                continue

            unique = True

            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    unique = False
                    break

            if unique:
                return nums[i]

        return -1