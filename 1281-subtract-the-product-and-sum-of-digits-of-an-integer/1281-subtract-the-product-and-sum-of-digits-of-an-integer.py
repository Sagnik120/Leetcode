class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=0
        m=1
        while n!=0:
            r=n%10
            s+=r
            m*=r
            n//=10
        return m-s