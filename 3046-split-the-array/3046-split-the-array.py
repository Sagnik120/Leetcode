class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        frq=Counter(nums)

        for count in frq.values():
            if count>2:
                return False
        return True