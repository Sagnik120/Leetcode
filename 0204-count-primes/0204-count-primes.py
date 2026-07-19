class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        size = n // 2
        is_prime = [True] * size
        is_prime[0] = False
        
        for i in range(1, int(n**0.5) // 2 + 1):
            if is_prime[i]:
                p = 2 * i + 1
                start_index = (p * p) // 2
                is_prime[start_index::p] = [False] * len(is_prime[start_index::p])
                
        return 1 + sum(is_prime)