class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        s=set()
        left=0
        right=len(nums)-1
        avg=0   
        while right>=left:
            avg=(nums[right]+nums[left])/1
            s.add(avg)
            right-=1
            left+=1

        return len(s)