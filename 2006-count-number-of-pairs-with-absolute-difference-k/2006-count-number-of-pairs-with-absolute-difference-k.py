class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        frq={}
        ans=0
        for num in nums:
            ans+=frq.get(num-k,0)
            ans+=frq.get(num+k,0)

            frq[num]=frq.get(num,0)+1
        return ans