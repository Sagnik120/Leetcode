class Solution:
    def minimumFlips(self, n: int) -> int:
        if n==0 or n==(2**n.bit_length())-1:
            return 0
        s=bin(n)[2:]
        rev=s[::-1]
        flip=0
        for i in range(len(s)):
            if s[i]!=rev[i]:
                flip+=1
        return flip
