class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        m1=0
        m2=0
        for i in range(k):
            m1+=nums[i]
            m2+=nums[len(nums)-i-1]
        return abs(m1-m2)