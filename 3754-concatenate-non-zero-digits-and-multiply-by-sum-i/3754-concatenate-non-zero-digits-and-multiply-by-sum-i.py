class Solution:
    def sumAndMultiply(self, n: int) -> int:
        def reverse(n):
            rev = 0
            while n:
                r = n % 10
                if r != 0:
                    rev = rev * 10 + r
                n //= 10
            return rev

        def reverse1(n):
            rev = 0
            s = 0

            while n:
                r = n % 10
                rev = rev * 10 + r
                s += r
                n //= 10

            return rev * s

        return reverse1(reverse(n))