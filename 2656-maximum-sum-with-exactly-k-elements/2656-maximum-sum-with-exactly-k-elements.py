class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        s=max(nums)

        a=s+1
        for i in range(k-1):
            s+=a
            a+=1
        return s