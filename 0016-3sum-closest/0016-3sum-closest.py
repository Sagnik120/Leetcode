class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        max_diff = float('inf')
        ans=float('inf')
        for i in range(0,n-1):
            l=i+1
            r=n-1
            s=0
            while r>l:
                s=nums[l]+nums[r]+nums[i]
                if(abs(s-target)<max_diff):
                    max_diff=abs(s-target)
                    ans=s
                if s==target:
                    return s
                elif s>target:
                    r-=1
                else:
                    l+=1
        return ans