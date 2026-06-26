class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        sum1=0
        ans=0
        p=1
        for i in range(31):
            sum1=0
            for num in nums:
                if (num>>i) & 1==1:
                    sum1+=1
            if(sum1>=k):
                ans+=p
                p*=2
            else:
                p*=2
        return ans
            