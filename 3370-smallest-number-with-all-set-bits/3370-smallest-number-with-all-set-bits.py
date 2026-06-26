class Solution:
    def smallestNumber(self, n: int) -> int:
        m=n.bit_length()
        return (2**m)-1