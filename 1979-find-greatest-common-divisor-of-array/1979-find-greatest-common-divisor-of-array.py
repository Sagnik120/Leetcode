class Solution:
    def findGCD(self, nums: List[int]) -> int:
        m1=max(nums)
        m2=min(nums)

        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        return gcd(m1,m2)