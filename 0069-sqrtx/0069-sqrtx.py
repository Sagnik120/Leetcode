class Solution:
    def mySqrt(self, x: int) -> int:
        low=0
        high=x
        ans=0
        while high>=low:
            mid=low+((high-low)>>1)
            m=mid*mid
            if m==x:
                return mid
            elif m<x:
                ans = mid
                low=mid+1
            else:
                high=mid-1
        return ans