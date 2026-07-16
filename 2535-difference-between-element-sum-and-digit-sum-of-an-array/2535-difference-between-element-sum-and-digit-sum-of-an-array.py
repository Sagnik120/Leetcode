class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s1=sum(nums)
        s2=0
        for i in range(len(nums)):
            if nums[i]<9:
                s2+=nums[i]
            else:
                s=str(nums[i])
                n=0
                for i in range(len(s)):
                    n+=int(s[i])
                s2+=n
        return abs(s1-s2)
