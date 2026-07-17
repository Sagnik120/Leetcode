class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime = [True for _ in range(n + 1)]
        p = 2
        while p * p <= n:
            if prime[p]:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        primes = sum(prime[2:])
        return math.factorial(primes) * math.factorial(n - primes) % (10 ** 9 + 7)