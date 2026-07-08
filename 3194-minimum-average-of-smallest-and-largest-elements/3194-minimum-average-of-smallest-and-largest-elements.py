class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()

        l=0
        h=len(nums)-1
        m=float('inf')
        while h>=l:
            avg=(nums[l]+nums[h])/2
            m=min(m,avg)
            h-=1
            l+=1
        return m