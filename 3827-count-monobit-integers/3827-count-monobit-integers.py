class Solution:
    def countMonobit(self, n: int) -> int:
        if n==0:
            return 1
        return math.floor(math.log2(n + 1)) + 1