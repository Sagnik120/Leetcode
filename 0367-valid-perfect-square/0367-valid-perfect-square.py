class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=0
        h=num

        while  l<=h:
            mid=l+((h-l)>>2)
            s=mid*mid
            if s==num:
                return True
            elif s<num:
                l=mid+1
            else:
                h=mid-1
        return False