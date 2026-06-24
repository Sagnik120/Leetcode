class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt=Counter(nums)

        for feq in cnt.values():
            if feq & 1 !=0:
                return False
        return True
