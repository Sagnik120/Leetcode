class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        m=float("inf")

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]==nums[j]==nums[k]:
                        m=min(abs(i-j)+abs(j-k)+abs(k-i),m)
        return -1 if m==float("inf") else m