class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s=set()

        for num in nums:
            if num%k==0:
                s.add(num)

        s=sorted(s)

        m=k
        for num in s:
            if m not in s:
                return m
            m=m+k
        return m