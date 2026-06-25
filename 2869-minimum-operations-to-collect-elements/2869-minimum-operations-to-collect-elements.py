class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        counter=0
        seen=set()
        for i in range(len(nums)-1,-1,-1):
            counter+=1
            if nums[i]<=k:
                seen.add(nums[i])
            if len(seen)==k:
                return counter